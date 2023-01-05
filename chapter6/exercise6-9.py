
favorite_places ={
    'YH':['KunMing','AnNing'],
    'YB':['DaLi','LiJiang']
}

for name,places in favorite_places.items():
    print("\nName: " + name.title())
    for place in places:
        print("\t" + place)