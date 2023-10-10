import os
import json
import requests
import xmltodict

from airflow.decorators import dag, task
import pendulum
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

# Constants
PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
EPISODE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "episodes")
FRAME_RATE = 16000
os.makedirs(EPISODE_FOLDER, exist_ok=True)


@dag(
    dag_id='podcast_summary',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2022, 5, 30),
    catchup=False,
)
def podcast_summary():

    @task()
    def get_episodes():
        response = requests.get(PODCAST_URL)
        feed = xmltodict.parse(response.text)
        episodes = feed["rss"]["channel"]["item"]
        print(f"Found {len(episodes)} episodes.")
        return episodes

    @task()
    def load_episodes(episodes):
        hook = SqliteHook(sqlite_conn_id="podcasts")
        stored_episodes = hook.get_pandas_df("SELECT * from episodes;")
        new_episodes = [
            [episode["link"], episode["title"], episode["pubDate"], episode["description"], f"{episode['link'].split('/')[-1]}.mp3"]
            for episode in episodes if episode["link"] not in stored_episodes["link"].values
        ]

        hook.insert_rows(table='episodes', rows=new_episodes, target_fields=["link", "title", "published", "description", "filename"])
        return new_episodes

    @task()
    def download_episodes(episodes):
        downloaded_files = []
        for episode in episodes:
            filename = f"{episode[4]}.mp3"  # Using index 4 because episode is a list containing filename at index 4
            audio_path = os.path.join(EPISODE_FOLDER, filename)
            if not os.path.exists(audio_path):
                print(f"Downloading {filename}")
                audio_data = requests.get(episode["enclosure"]["@url"]).content
                with open(audio_path, "wb+") as file:
                    file.write(audio_data)
            downloaded_files.append({"link": episode[0], "filename": filename})
        return downloaded_files

    @task()
    def speech_to_text(audio_files):
        hook = SqliteHook(sqlite_conn_id="podcasts")
        untranscribed_episodes = hook.get_pandas_df("SELECT * from episodes WHERE transcript IS NULL;")

        model = Model(model_name="vosk-model-en-us-0.22-lgraph")
        recognizer = KaldiRecognizer(model, FRAME_RATE)
        recognizer.SetWords(True)

        for row in untranscribed_episodes.iterrows():
            filepath = os.path.join(EPISODE_FOLDER, row["filename"])
            audio = AudioSegment.from_mp3(filepath).set_channels(1).set_frame_rate(FRAME_RATE)
            transcript = ""

            step = 20000
            for i in range(0, len(audio), step):
                segment = audio[i:i+step]
                recognizer.AcceptWaveform(segment.raw_data)
                result = recognizer.Result()
                text = json.loads(result)["text"]
                transcript += text

            hook.insert_rows(table='episodes', rows=[[row["link"], transcript]], target_fields=["link", "transcript"], replace=True)

    # Tasks execution order
    podcast_episodes = get_episodes()
    create_database = SqliteOperator(
        task_id='create_table_sqlite',
        sql="""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT,
            transcript TEXT
        );
        """,
        sqlite_conn_id="podcasts"
    )
    create_database >> podcast_episodes >> load_episodes() >> download_episodes()  # >> speech_to_text()

    # Uncomment the last part of the chain (speech_to_text) if needed

podcast_summary_instance = podcast_summary()
