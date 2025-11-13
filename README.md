# 🏏 Cricket Score Predictor (CSP App)

A machine learning–powered web application that predicts the **final score of a T20 cricket inning** based on the current match situation.  
Built using **Flask**, **Python**, **Bootstrap**, and a trained **ML regression model**.

---

## 🚀 Features

- Predicts final score using:
  - Batting team
  - Bowling team
  - Venue (city)
  - Current score
  - Overs completed
  - Wickets fallen
  - Last 5-over runs
- Clean, responsive UI using Bootstrap
- Dynamic team images (auto-updates as you pick the team)
- Easy-to-run Flask backend
- Fully customizable ML model (pickle file)

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | HTML5, CSS3, Bootstrap |
| Backend | Flask (Python) |
| ML Model | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Deployment | Localhost / Any cloud platform |

---

## 🎯 How It Works

The app collects the following inputs from the user:

Batting Team

Bowling Team

Venue

Current Score

Overs Completed

Wickets Fallen

Runs in Last 5 Overs

These features are passed to a trained machine learning model stored in model.pkl, which predicts the final score of the innings.

## 🧠 Machine Learning

You can use any regression-based ML model such as:

Linear Regression

Random Forest

Gradient Boosting

XGBoost

Ridge / Lasso

Ensure the preprocessing pipeline is included inside the .pkl.

