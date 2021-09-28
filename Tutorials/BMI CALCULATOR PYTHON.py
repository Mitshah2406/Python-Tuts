def bmicalci(weight_in_kg, height_in_meters):
    return weight_in_kg / (pow(height_in_meters, 2))


weight = float(input('Enter the weight(kg) : '))
height = float(input('Enter the height(m) : '))
result = bmicalci(weight, height)
print(f"The {'result'} value is ", result)