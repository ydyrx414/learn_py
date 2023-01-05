favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("Sarah's favorite langage is " + 
    favorite_language['sarah'].title() + ".")

#6-3-1
for name,langage in favorite_language.items():
    print(name.title() + "'s favorite language is " +
    langage.title() + ".")

#6-3-2
for name in favorite_language.keys():
    print(name.title())

friends = {'phil','sarah'}
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is "+
        favorite_language[name].title())