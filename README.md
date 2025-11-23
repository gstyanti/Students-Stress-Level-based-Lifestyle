**⭐ Project Overview**
This project uses a dataset sourced from Kaggle to analyze and predict students stress levels based on their daily lifestyle habits.
The primary goal is to provide insights that can help parents and teachers become more aware of students mental well being, ensuring
that academic activities do not become overwhelming or excessively stressful. By understanding the key factors that influence student 
stress, learning can become a more enjoyable and healthier experience.

**🎯 Project Objectives**
- Identify lifestyle factors that influence student stress levels
- Build a machine learning model to predict stress categories (Low = 0, Moderate = 1, High = 2)
- Provide feature importance analysis to help educators and parents understand the most impactful variables
- Deploy an interactive Streamlit application to demonstrating real time prediction.

**📌 Variables Included**
The dataset contains lifestyle related features such as:
- Study Hours       : Daily study duration
- Extracurricular   : Time spent in extracurricular aactivities
- Sleep Hours       : Daily sleep duration
- Social Hours      : Time spent socializing
- Physical Activity : Duration of physical exercise
- GPA               : Academic performance index
- Stress Level      : Target variable used for prediction

**🤖 Model & Feature Analysis**
A random Forest Classifier model was used for prediction. Based on the feature importance results, the three most influential factors 
affecting students stress levels are:
1. Study Hours per Day
2. Sleep Hour per Day
3. GPA
Meanwhile, Physical Activity, Social Hours, & Extracurricular Hours ranked at the bottom in terms of importance, indicating that these
variables contribute minimally to predicting stress levels in the model.

**💡 Key Insight**
Students stress is primarily influenced by:
- Length of study time per day
- Sleep quality and duration
- Academic performance (GPA)
These insights can help parents and educators maintain a healty balnce between academic demands and lifestyle habits to support better
mental health and learning environtment.

⛓️‍💥 App Predict Public : https://students-stress-level-based-lifestyle-byantiiii.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-brightgreen)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange)
