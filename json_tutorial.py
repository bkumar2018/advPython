import json


person = {"name":"John", "age":23, "city": "Pune", "titles":["engg","prog","test","java"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# with open("persons.json", 'w') as jfile:
#     json.dump(person,jfile,indent=4)

#load json file and make it to dict
with open('persons.json', 'r') as file:
    person = json.load(file)
    print(person)
