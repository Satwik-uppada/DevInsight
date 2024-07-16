# DevInsight - Developer Salary Prediction based on Stack Overflow Survey Data 2023
Predict developer salaries with our app! Analyze factors like country, education, and experience. Gain insights for informed decisions. Try it now!
![Salary](https://github.com/Satwik-uppada/Salary-Prediction-Based-On-Stack-Overflow-Developer-Survey-Using-Machine-Learning/assets/92086645/cecd3b44-f163-4943-91f9-95671469b79d)

Certainly! Here's an updated README that includes information about GridSearchCV and the IPython Notebook files:

---

# DevInsight 📊💼

DevInsight is an interactive web application designed to analyze and predict developer salaries based on key factors such as country, education level, and years of experience. This project leverages machine learning models to provide accurate salary estimations, coupled with insightful data visualizations derived from the latest Stack Overflow Developer Survey data (2023).

---

## Getting Started 🚀

### Clone the Repository

To get a local copy of DevInsight up and running on your machine, follow these steps:

```bash
https://github.com/Satwik-uppada/Salary-Prediction-Based-On-Stack-Overflow-Developer-Survey-Using-Machine-Learning.git
cd Salary-Prediction-Based-On-Stack-Overflow-Developer-Survey-Using-Machine-Learning
```

### Install Dependencies

Make sure you have Python installed. Then, install the required Python packages using pip:

```bash
pip install streamlit pandas numpy scikit-learn seaborn matplotlib
```

### Run the Application

Use Streamlit to launch the DevInsight application:

```bash
streamlit run app.py
```

Access the application in your web browser at `http://localhost:8501`.

---

## Pages Overview 📄

### 1. **Predict Page**

The Predict page allows you to input your details and receive an estimated salary prediction based on:
- **Country**: Select your country from the dropdown menu.
- **Education Level**: Choose your highest level of education completed.
- **Years of Experience**: Adjust the slider to indicate your professional coding experience in years.

### 2. **Explore Page**

The Explore page provides interactive visualizations and insights from the Stack Overflow Developer Survey data (2023). Explore various aspects such as:
- **Main Branches**: Distribution of developers across different main branches.
- **Age Groups**: Demographic breakdown of developers by age.
- **Employment Type**: Insights into various employment types among developers.
- **Work Environment**: Analysis of developers' remote work preferences.
- **Coding Activities**: Popular coding activities among developers.
- **Education Level**: Distribution of developers based on their educational qualifications.
- **Years of Coding Experience**: Distribution of developers by years of coding experience.
- **Years of Professional Experience**: Distribution of developers by years of professional coding experience.

---

## Models and Techniques Used 🤖

### Machine Learning Models

- **Linear Regression**: Trained on the cleaned and preprocessed Stack Overflow survey data to predict developer salaries based on input features.
- **Decision Tree Regression**: Employed for comparison with the linear regression model, offering an alternative approach to salary prediction.
- **Random Forest Regression**: Utilized to enhance prediction accuracy by aggregating multiple decision tree regressors.
- **GridSearchCV**: Applied to optimize hyperparameters for the Decision Tree Regression model, improving its performance.

### Jupyter Notebook Files

- **SalaryPrediction.ipynb**: Jupyter Notebook containing the data preprocessing, model training, and evaluation steps for salary prediction.
- **model.ipynb**: Jupyter Notebook showcasing the development and training of machine learning models using the Stack Overflow survey data.

---

## Technologies Used 🛠️

- **Python**: Core programming language.
- **Pandas, NumPy**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning models for salary prediction.
- **Streamlit**: Web application framework for interactive UI.
- **Matplotlib, Seaborn**: Data visualization libraries.

---

## Contributing 💡

Contributions to DevInsight are welcome! If you encounter any issues or have suggestions for improvements, feel free to submit an issue or pull request through GitHub.


---


[Download dataset here](https://survey.stackoverflow.co/)

---

[12111298 B50.pdf](https://github.com/user-attachments/files/16143893/12111298.B50.pdf)
