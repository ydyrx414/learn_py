persons = {
    'YB' : {
        'age':20,
        'sex':'man'
    },

    'HH':{
        'age':20,
        'sex':'man'
    }
}

for name,info in persons.items():
    print("\nName: " + name.title())
    age = info['age']
    sex = info['sex']
    print("Age: " + str(age))
    print("Sex: " + sex.title())