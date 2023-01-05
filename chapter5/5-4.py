requested_oppings = ['mushrooms','green peppers','extra cheese']

for requested_opping in requested_oppings:
    print(("Adding " + requested_opping + "."))

print("\nFinished making your pizza!")

for requested_opping in requested_oppings:
    if requested_opping == 'green peppers':
        print("Sorry, we are out of green pepers right now")
    else:
        print(("Adding " + requested_opping + "."))

print("\nFinished making your pizza!")
