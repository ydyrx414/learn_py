rivers = {'nile':'egypt','Mekong':'china','amazon':'peru'}

for river,nation in rivers.items():
    print("The " + river.title() + " runs through " + nation.title())

for river in rivers.keys():
    print(river.title())

for nation in rivers.values():
    print(nation.title())