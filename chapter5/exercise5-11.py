Nums = [1,2,3,4,5,6,7,8,9]
print(Nums)

for num in Nums:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')