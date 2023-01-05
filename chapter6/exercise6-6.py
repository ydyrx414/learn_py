favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = {'jen': 'python','sarah': 'c'}

for name in favorite_language.keys():
    if name in names.keys():
        print("Thank you for your participation")
    else:
        print("Please take the investigation")


