print("DATA CONVERSION UTILITY")

product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_price = price * quantity
amount_str = str(total_price)

print("\nTYPE CASTING SUMMARY")

print("Variable\t\tValue\t\tPython Type")
print("product_name\t\t", product_name, "\t\t", type(product_name))
print("price\t\t\t", price, "\t\t", type(price))
print("quantity\t\t", quantity, "\t\t", type(quantity))
print("total_price\t\t", total_price, "\t\t", type(total_price))
print("amount_str\t\t", amount_str, "\t\t", type(amount_str))

print("\nTAX INVOICE")
print("Product Name :", product_name)
print(f"Price per Unit: Rs. {price:.2f}")
print("Quantity      :", quantity)
print("Invoice Total: Rs.", amount_str)