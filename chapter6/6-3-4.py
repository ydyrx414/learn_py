favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")

for language in favorite_language.values():
    print(language.title())

print("\n")

for language in set(favorite_language.values()):
    print(language.title())