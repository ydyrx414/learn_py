favorite_languages = {
    'jen': ['python','c'],
    'sarah': ['c','ruby'],
    'edward': ['ruby'],
    'phil': ['python','c']
}

for name,languages in favorite_languages.items():
    if(len(languages)==1):        
        print("\n" + name.title() + "'s favorite language is" + str(languages))
    
    print("\n" + name.title() +"'s favorite language are:")
    for language in languages:
        print("\t" + language.title())