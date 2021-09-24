# Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:

#  BMI = (weight in Kg)/(Height in Meters)^2.

# Write python code which can accept the weight and height of a person and calculate his BMI.

# note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def BMI_calci(w, h):
    result = (w)/(pow(h, 2))
    return result


weight_in_kg = float(input("Enter Your Weight: "))
height_in_meters = float(input("Enter Your Height: "))

BMI = BMI_calci(weight_in_kg, height_in_meters)
print("The Body Mass Index(BMI) is: ", BMI)
