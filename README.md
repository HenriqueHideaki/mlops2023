# DCA0305 - MACHINE LEARNING-BASED SYSTEMS DESIGN

### Student Information

**Student:** Henrique Hideaki Koga

**Registration Number:** 2022044055

**Course Overview**
- Course Code: DCA0305
- Credit Hours: 60 hours
- Responsible Unit: Department of Computer Engineering and Automation
- Course Type: Discipline

**Syllabus**
- Machine Learning Development Lifecycle
- Data Preparation, Feature Engineering, and Model Selection
- Data and Reference Models Definition
- Data and Model Quality Assessment, Monitoring
- Data and Model Quality Assessment, Monitoring
- Model Update Algorithms
- Model Personalization Solutions
- Scaling Machine Learning Models in Production
- Case Studies in System Integration with Machine Learning Models

**Projects**
**Movie Recommendation System With Python And Pandas: Data Project**
  - This project involves creating a movie recommendation system using Python and Pandas. It focuses on collecting and analyzing movie data to provide personalized recommendations to users based on their preferences and viewing history.

**Apache Airflow Podcast Data Pipeline Project**

The aim of this project is to create a four-stage data pipeline using Apache Airflow to automate the collection, storage, and transcription of podcast episodes.

**Episode Collection:** Episodes are fetched from a podcast feed through HTTP requests and parsed into Python data.

**Episode Loading:** New episodes are identified and inserted into a SQLite database for further processing.

**Episode Download:** The identified new episodes are downloaded from the web and stored locally as audio files.

**Speech-to-Text Transcription:** The downloaded episodes are transcribed using a speech recognition model, and the transcriptions are stored in the database.

This project provides a hands-on opportunity to build skills in data engineering, task scheduling, error handling, and using Apache Airflow.

**Important Practices to Follow**
- **Code Refactoring**: Refactoring is not just a one-time activity but an ongoing process. Well-refactored code is easier to understand, debug, and maintain. We strongly encourage you to refactor your code as you progress with your projects.
- **Clean Code Principles**: Writing clean code is essential for the long-term maintainability of your projects. Follow principles like DRY (Don't Repeat Yourself) and KISS (Keep It Simple) to make your code more effective and easier to understand.
- **Linting**: A linting score of at least 9/10 is required for this assignment. Utilize tools like pylint to analyze your code and adhere to best practices.
- **Exception Handling**: Proper exception handling can make your code robust and easier to debug. Use Python’s try, except, and finally blocks to catch and handle exceptions gracefully.
- **Logging**: Include logging in your projects to capture runtime information, which can be invaluable for debugging and monitoring your code's behavior. Use Python’s built-in logging library to include logs at various levels such as INFO, DEBUG, and ERROR.
- **Unit Testing**: The inclusion of unit tests is mandatory. Tests validate that your code works as expected and make it easier for future you or other developers to change the code with confidence.
- **GitHub Codespaces**: Leverage GitHub Codespaces for prototyping and initial development. Codespaces provide a complete, configurable dev environment that allows you to code directly within GitHub.
- **Command Line Interface (CLI)**: Implement a Command Line Interface to allow users to interact with your project easily. This is crucial as it offers a versatile way of running different functionalities and options in your code.

**Prerequisites**
- Python 3.8+
- Airflow 2.3+
- Pandas: `pip install pandas`
- sqlite3: follow these instructions
- xmltodict: `pip install xmltodict`
- requests: `pip install requests`

*Note: You will run the code on your local machine, so you need to set up your computer properly and install the necessary packages.*

This course offers valuable insights into machine learning-based systems design and equips students with essential skills for building, maintaining, and deploying machine learning models in real-world scenarios. By the end of this course, students will have the knowledge and hands-on experience needed to excel in the field of machine learning-based systems design.
