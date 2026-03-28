# Main module or module 3: For displaying the interface to user and ask him his symptoms and give results

import mod2 #we are using module 2 which is our core logic or prediction system

def main():
    print()
    print("Diabetes Risk Prediction System")
    print()
    print("Welcome! Please enter the details below to check diabetes risk.")
    print()

    while True:
        print("Please enter the patient's health details.")
        
        # Getting the numbers from the user

        while True:
            glucose = float(input("Enter Glucose level in (mg/dL): "))
            if 0 < glucose < 300: #To make sure that user doesnt enter a invalid input
                break
            print("Please enter a valid glucose level (between 0 and 300)") 

        while True:
            bp = float(input("Enter Blood Pressure in (mm Hg): "))
            if 0 < bp < 200:
                break
            print("Please enter a valid blood pressure (between 0 and 200)")
        
        while True:
            bmi = float(input("Enter BMI: "))
            if 0 < bmi < 70:
                break
            print("Please enter a valid BMI (between 0 and 70)")

        while True:
            age = float(input("Enter Age: "))
            if 0 < age < 120:
                break
            print("Please enter a valid age (between 0 and 120)")

        
        
        selected_symptoms = [glucose, bp, bmi, age] # Grouping the inputs together
        
        
        result = mod2.predict_risk(selected_symptoms)  # sending the inputs to mod2 for prediction.
        
        print()
        print("Predicted Results")
        
        # Displaying results
        if result == 1:
            print("Result: High Risk of Diabetes")
            print("Your values are closer to the diabetic group in most checks.")
        else:
            print("1. Disease: Low Diabetes Risk")
            print(" Your values are NOT closer to the diabetic group in most checks.")
            
        # Checking if user wants to run it again
        choice = input("Do you want to check for another patient? (yes/no): ")
        if choice != 'yes':
            print()
            print("Thankyou for using our system :)")
            break
        print()
main()