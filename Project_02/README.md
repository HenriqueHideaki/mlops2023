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

## Pylint Analysis for `podcast.py`

### Style and Formatting
- **Long Lines (C0301)**: Some lines exceed 100 characters. Adjust for better readability.
- **Missing Newline at End (C0304)**: Add a newline at the end of the file.
- **Naming Convention (C0103)**: The constant `summary` should be named in UPPER_CASE.

### Documentation
- **Module Docstring (C0114)**: The module requires a docstring to describe it.

### Errors and Warnings
- **Import Issue (E0401)**: Problem importing `requests`.
- **Unused Variables (W0612)**: Variables like `new_episodes` are not being used.
- **Undefined Variable (E1120)**: The variable `pendulum` is not defined.
- **Assignment (expression-not-assigned)**: Check the assignments of expressions.
- **Missing Arguments (E1120)**: The `episodes` argument is missing in function calls.

### Overall Score
The code received a score of 5.52/10 from pylint, showing an improvement from the previous score of 2.36/10.

### Notes on Improvements
Since the last analysis, there has been a notable improvement in the code score, moving from 2.36 to 5.52. This suggests that several previously identified issues have been addressed and rectified. Enhancements in style, formatting, and error correction contributed to this uplift. Continuing to use tools like pylint regularly will help maintain and further improve code quality. The recommendation is to keep reviewing and refactoring the code to address any remaining issues and to always strive to adopt best coding practices.
<a href="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/airflow__pylint_01.jpg">
    <img src="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/airflow__pylint_01.jpg" alt="airflow" width="500"/>
</a>

<a href="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/airflow__pylint_03.jpg">
    <img src="https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_02/airflow__pylint_03.jpg" alt="airflow" width="700"/>
</a>


## How to Use

1. **Configuration**: Set up the environment ensuring all dependencies are installed and services (like Apache Airflow) are running.
2. **Customization**: Adapt the code as necessary to cater to your specific needs, such as pointing to different podcast sources or adjusting transcription parameters.
3. **Execution**: Start the scripts or DAGs and monitor the process through the provided interfaces (like Apache Airflow's web interface).









