#This is the core logic and predicts the risk of diabetes on the basis of average of diabetic and healthy person.

import mod1

def predict_risk(user_input):
    # Loads the database
    df = mod1.load_database()
    
    # This takes the user inputs.
    user_glucose = user_input[0]
    user_bp = user_input[1]
    user_bmi = user_input[2]
    user_age = user_input[3]
    
    # Here we are making two groups from our dataset, persons with diabetes and healthy.
    healthy_people = df[df['Outcome'] == 0]
    diabetic_people = df[df['Outcome'] == 1]
    
    risk_score = 0 #Here ive set a counter which is intially at zero.
    
    # Checking for Glucose
    difference_diabetic_glu = abs(user_glucose - diabetic_people['Glucose'].mean())
    difference_healthy_glu = abs(user_glucose - healthy_people['Glucose'].mean())
    if difference_diabetic_glu < difference_healthy_glu:
        risk_score = risk_score + 1
        
    # Checking for blood pressure
    difference_diabetic_bp = abs(user_bp - diabetic_people['BloodPressure'].mean()) # checking mean for diabetic case
    difference_healthy_bp = abs(user_bp - healthy_people['BloodPressure'].mean())  # checking mean for healthy case

    if difference_diabetic_bp < difference_healthy_bp:
        risk_score = risk_score + 1

    # Checking BMI
    difference_diabetic_bmi = abs(user_bmi - diabetic_people['BMI'].mean())
    difference_healthy_bmi = abs(user_bmi - healthy_people['BMI'].mean())

    if difference_diabetic_bmi < difference_healthy_bmi:
        risk_score = risk_score + 1
        
    # Checking age
    difference_diabetic_age = abs(user_age - diabetic_people['Age'].mean())
    difference_healthy_age = abs(user_age - healthy_people['Age'].mean())
    if difference_diabetic_age < difference_healthy_age:
        risk_score = risk_score + 1

    # Here we are taking Final decision, if they match the average of diabetic person in two or more than two categories, Then we mark it as high risk.
    if risk_score >= 2:
        return 1
    else:
        return 0