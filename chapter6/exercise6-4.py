favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name,languang in favorite_language.items():
    print(name.title() + ':' + languang.title())

favorite_language['YB'] = 'hhh'
favorite_language['YH'] = 'jjj'

for name, languang in favorite_language.items():
    print(name.title() + ':' + languang.title())
