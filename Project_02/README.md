# Build an Airflow Data Pipeline to Download Podcasts
This project aims to provide automated tools for handling and analyzing podcast episodes. Using modern technologies and advanced libraries, we seek to simplify the workflow for podcast producers and enthusiasts.

<p align="center">
  <a href="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/podcast_airflow.png">
    <img src="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/podcast_airflow.png" alt="podcast airflow" width="800"/>
  </a>
</p>




## Overview

The platform offers a range of functionalities, from searching and storing podcast episodes to their transcription and analysis. Automation is key to ensuring that the latest content is always processed and available for analysis.

## Features

- **Automatic Episode Fetching**: Our solution regularly checks podcast sources to identify and download new episodes.
- **Audio Transcription**: Automatically convert the audio content of episodes into text to facilitate analysis and accessibility.
- **Content Analysis**: Delve into the transcribed content to gain insights on the topics covered in the episodes.

## Installation Requirements

- Python 3.8 or higher.
- Apache Airflow: For task automation and orchestration.
- SQLite: Used for episode data storage.
- Other Python libraries: `requests`, `xmltodict`, `vosk`, `pydub`.

## Installation Guide

1. **Clone the Repository**:
    ```
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Virtual Environment**:
   It's recommended to create a virtual environment for installing the project's dependencies:
    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```
## Functions Overview

### `podcast_summary()`
This is the main DAG function. It orchestrates the execution order of various tasks that fetch, store, download, and transcribe podcast episodes.

### `get_episodes()`
- **Purpose**: Fetch the list of podcast episodes from the given `PODCAST_URL`.
- **Output**: Returns a list of episodes with their respective details.

### `load_episodes(episodes)`
- **Purpose**: Store new podcast episodes in a SQLite database.
- **Input**: List of episodes to check against the database and store if they are new.
- **Output**: Returns a list of new episodes that were stored in the database.

### `download_episodes(episodes)`
- **Purpose**: Download the audio files of the provided podcast episodes.
- **Input**: List of episodes to download.
- **Output**: Returns a list of filenames that were successfully downloaded.

### `speech_to_text(audio_files)`
- **Purpose**: Transcribe the audio of podcast episodes into text.
- **Input**: List of audio files to transcribe.
- **Note**: The function uses the Vosk library for transcription and stores the transcriptions back into the SQLite database.

## How to Use

1. **Configuration**: Set up the environment ensuring all dependencies are installed and services (like Apache Airflow) are running.
2. **Customization**: Adapt the code as necessary to cater to your specific needs, such as pointing to different podcast sources or adjusting transcription parameters.
3. **Execution**: Start the scripts or DAGs and monitor the process through the provided interfaces (like Apache Airflow's web interface).









