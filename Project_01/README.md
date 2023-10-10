
# Movie Recommendation System With Python And Pandas: Data Project
[https://github.com/HenriqueHideaki/mlops2023/blob/main/Project_01/movie_recomendation.png](movie_recomendation_system)
## Author
Henrique Hideaki Koga  
Registration Number: 2022044055  
Federal University of Rio Grande do Norte  
Department of Computer Engineering and Automation (DCA)
## Introduction

# Movie Recommendation System with Python and Pandas: Data Project

The "Movie Recommendation System with Python and Pandas" is an interactive and engaging data project that delves into the world of machine learning and data analysis to create a system that provides personalized movie suggestions based on user preferences. This project serves as a practical demonstration of how data science can be applied to enhance users' entertainment experience by helping them discover movies that align with their interests.

## Project Objective

The primary objective of this project is to develop an effective and user-friendly movie recommendation system, allowing users to explore a wide variety of films based on their preferences. To achieve this goal, several data processing, modeling, and interactivity steps are incorporated into the project.

## Key Features

1. **Data Loading:** The project begins by importing essential data, including detailed movie information and user-provided ratings. This data forms the foundation for the recommendation system.

2. **Text Preprocessing:** Movie titles undergo preprocessing to remove special characters and ensure accurate textual analysis. This is crucial for calculating similarity between movies based on their titles.

3. **TF-IDF Vectorization:** A TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer is created to convert movie titles into numerical representations. This enables comparison and matching of movies based on their titles.

4. **Interactive Movie Search:** Users have the opportunity to input the title of a movie of their choice. The system utilizes the TF-IDF vectorizer to identify similar movies based on the user-entered title. Movies with the best textual match are presented as suggestions.

5. **Personalized Recommendations:** In addition to title-based searches, the system also offers personalized recommendations based on user preferences and viewing history. This is achieved through collaborative filtering techniques, identifying users with similar tastes and recommending highly-rated movies from those users.

## Usage and Learning

This project provides a unique opportunity for data enthusiasts and aspiring data scientists to delve deeper into data processing, modeling, and creating interactive systems. It demonstrates the practical application of machine learning concepts and text analysis to solve a real-world problem—helping users discover movies that align with their individual tastes.

By interacting with this project, users can experience how recommendation algorithms work in practice and gain insights into how recommendation systems are implemented on online entertainment platforms.

Embark on this cinematic discovery journey with the "Movie Recommendation System with Python and Pandas" and explore a world of movies that cater to your personal preferences.


# Requirements and Technologies Used

This project requires the use of the following technologies and meets specific requirements:

## Technologies Used

- Python 3.8 or higher: The programming language used to develop the project.
- Pandas: A Python library for data manipulation and analysis.
- Regex: Used for regular expressions, assisting in text cleaning and manipulation.
- Numpy: A Python library for supporting multidimensional arrays and matrices.
- Ipywidgets: Used to create interactive graphical user interfaces in Jupyter Notebook.
- Scikit-learn: A Python library for machine learning and data mining.
- IPython: An interactive Python interface.
- Jupyter Notebook: A web application that allows the creation and sharing of documents containing live code, equations, visualizations, and narrative text.
- And other Python libraries as needed.

## Requirements

- To run the project, you need to have Python and the libraries listed above installed in your development environment.
- Ensure you have the necessary datasets available locally or access them according to the specified source in the project.
- It is recommended to use a Python virtual environment to avoid package conflicts with other projects.

Please make sure to meet these requirements before starting the project to ensure a suitable and smooth development environment.



# Installation Instructions

Follow these steps to set up and run the project on your local machine:

## Prerequisites

- Python 3.8 or higher installed on your system.
- Access to the necessary datasets or the ability to retrieve them from the specified source.

## Steps

1. **Clone the Repository:** Start by cloning this project repository to your local machine using Git. Open your terminal or command prompt and run the following command:


2. **Navigate to the Project Directory:** Move to the project directory using the `cd` command:


3. **Create a Virtual Environment (Optional but Recommended):** It's a good practice to create a virtual environment for your project to manage dependencies. You can create a virtual environment using Python's built-in `venv` module. Run the following command to create a virtual environment:


Activate the virtual environment:

- **On Windows:**

  ```
  venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```
  source venv/bin/activate
  ```

4. **Install Dependencies:** Install the required Python libraries and dependencies using pip. Run the following command:



## Referências

- [Documentação Oficial do Pandas](https://pandas.pydata.org/docs/)
- [Tutorial de Sistemas de Recomendação com Python](#) (Substitua com um link relevante, se aplicável)
