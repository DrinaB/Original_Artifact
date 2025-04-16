from animal_shelter import AnimalShelter
from bson.objectid import ObjectId

animals = AnimalShelter("aacuser", "SNHU1234")

#valid document create
 'age_upon_outcome': "2 years",
 'animal_id': "test",
 'animal_type': "Dog",
 'breed': "Domestic Shorthair Mix",
 'color': "White",
 'date_of_birth': "2023-03-23",
 'datetime': "2023-03-23 11:14:00",
 'monthyear': "2023-03-23T11:14:00",
 'name': "Duke",
 'outcome_subtype': "",
 'outcome_type': 'Adoption',
 'sex_upon_outcome': "Spayed Male",
 'location_lat': 30.6525984560229,
 'location_long': -97.7419963476443,
 'age_upon_outcome_in_weeks': 53

#Invalid Document
print(animals.create({0:0}))


#Valid query
query = animals.read({"name": "Duke"})
for animal in query:
    print(animal)

#invalid query throws exception
print(list(animals.read({0:0})))
