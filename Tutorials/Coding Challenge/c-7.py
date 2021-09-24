# Write Python code which accepts name of a product and in turn returns their respective prices.

# Make sure to use dictionaries to store products and their respective prices.

# The dictionary should include at least 5 elements.

products = {"Chocolate": 'Rs10', "Icecream": 'Rs20',
            "Biscuit": 'Rs5', "Wafers": 'Rs15', "Cookies": 'Rs25'}
input_product=input("Enter the name of product: ")

if input_product in products:
    print(products[input_product])

else:
    print("Product not found.")
