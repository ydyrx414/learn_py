pets = {
    'pet1':{
        'master':'YB',
        'kind':'dog'
    },
    'pet2':{
        'master':'HH',
        'kind':'cat'
    }
}

for pet,info  in pets.items():
    print("\n" + pet.title())
    master = info['master']
    kind = info['kind']
    print("Kind: " + kind.title())
    print("Master: " + master.title())