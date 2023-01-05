available_topings = ['mushrooms','olives','green pepers','pepperoni','extra cheese']

requested_toppings = ['mushrooms','french frise','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_topings:
        print("Adding " + requested_topping + '.')
    else:
        print("Sorry,we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
