keys = ['type','name','genre','recently edited']
type = ['movie','movie','movie','book','book','book']
name = ['annie hall','wild strawberries','pulp fiction','war and peace','the god of small things','the road']
genre = ['rom com','drama','noir','epic','drama','dystopia']
recently_edited = ['False']
suggestions = dict.fromkeys(keys)
suggestions['type'] = type
suggestions['name'] = name
suggestions['genre'] = genre
suggestions['recently edited'] = recently_edited
for name , type, genre in zip(suggestions['name'], suggestions['type'], suggestions['genre']):
    print(f"{name}:{type}:{genre}")