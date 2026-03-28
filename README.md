# Diabetes Risk Predictor

It is a simple Python program that takes basic health details from the user and tells them whether they might be at risk of diabetes or not. It compares the user's values against the averages from a real dataset of many patients and gives a result.

---

## What it does

You enter 4 health values:
- Glucose level
- Blood Pressure
- BMI
- Age

The program then tells you whether your profile is High Risk or Low Risk for diabetes.

---

## Files in this project

| File | What it does |
|------|--------------|
| mod1.py | Loads the dataset |
| mod2.py | Contains the prediction logic |
| main.py | Main file, takes input from user and shows result |
| dataset.csv | The dataset used for prediction (patient records) |

---

## Dataset

This project uses the Pima Indians Diabetes Dataset which contains many rows of real patient data. The dataset is already included in this repository as dataset.csv so you do not need to download anything separately.

Downloaded it from here:
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
---

## How to set it up

Step 1 - Make sure Python is installed

Check by running:
python --version

Step 2 - Install pandas

pip install pandas

Step 3 - Make sure all files are in the same folder

Diabetes-Risk-Predictor/
├── dataset.csv
├── mod1.py
├── mod2.py
└── main.py

---

## How to run it

Open terminal or command prompt in the project folder and run:

python main.py

You will see something like this:

Diabetes Risk Prediction System

Welcome! Please enter the details below to check diabetes risk.

Please enter the patient health details.
Enter Glucose level in (mg/dL): 148
Enter Blood Pressure in (mm Hg): 85
Enter BMI: 33.6
Enter Age: 50

Predicted Results
Result: High Risk of Diabetes
Your values are closer to the diabetic group in most checks.

Do you want to check for another patient? (yes/no):

---

## Input ranges accepted

| Input | Valid Range |
|-------|-------------|
| Glucose | 0 to 300 mg/dL |
| Blood Pressure | 0 to 200 mm Hg |
| BMI | 0 to 70 |
| Age | 0 to 120 |

If you enter a value outside the range it will ask you to enter again.

---

Screenshots:
<img width="975" height="306" alt="image" src="https://github.com/user-attachments/assets/027e4b9d-5568-4efc-8035-ab74e76794c0" />
<img width="975" height="132" alt="image" src="https://github.com/user-attachments/assets/accf7525-dc0a-41d2-9bba-31792d092335" />


