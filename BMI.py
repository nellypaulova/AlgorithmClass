import math

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))
        height = height_cm / 100
        underweight = weight / 100
        normal = height / 100
        overweight = height / 100

        bmi_new = 1.3 * weight / height ** 2.5
        if bmi_new < 18.49: underweight = True
        elif 18.5 <= bmi_new < 25: underweight = False
        else:
            underweight = False

        if underweight: overweight = True
        else:
            overweight = False

        if bmi_new < 24.9: normal = True
        elif 25 <= bmi_new < 30: normal = False
        else: normal = False


        if bmi_new < 29.9: overweight = True
        elif 30 <= bmi_new < 40: overweight = False
        else:
            overweight = False

        print(f"Your BMI is: {bmi_new: .1f}")
        if underweight: print(f"Your BMI is underweight")
        elif normal: print(f"Your BMI is normal")
        else: print(f"Your BMI is overweight")
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter a number greater than 0")
    finally:
        print("Thank you for using this program that is greatly unreliable to actually tell you if you have a good body disposition.")

    answer = input("Do you wish to calculate again? (yes/no): ")
    if answer != "yes":
        break