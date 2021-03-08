# code here
from typing import Any

import json

# some dictionaries
p1 = { "name":"Father (Angelo)", "occupation":"Computer Engineer", "residence":"San Diego", "color":"orange"}
p2 = { "name":"Mother (Simona)", "occupation":"Stay at home mom", "residence":"San Diego", "color":"pink"}
p3 = { "name":"Me (Luca)", "occupation":"high schooler", "residence":"San Diego", "color":"green"}
p4 = { "name":"Brother (Davide)", "occupation":"Makes movies for rappers", "residence":"San Diego", "color":"blue"}
p5 = { "name":"Brother (Matteo)", "occupation":"Google Programmer", "residence":"San Diego", "color":"purple"}

# a list of dictionaries
family = [p1, p2, p3, p4, p5]
# write some code to Print List of people one by one
print("List of people")
print(type(family))
print(family)
for person in family:
    print(person['name'] + "," + person['occupation'] + "," + person['residence'] + "," + person['color'])
print()

# turn list to dictionary of people
dict_people = {'people': family}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)

# write some code to Print People from Dictionary
##list_of_people2 = dict_people ['people']
for person in dict_people['people']:
    print(person['name'] + " = " + person['occupation'] + " = " + person['residence'] + " = " + person['color'])
print()



# turn dictionary to JSON (aka string)
json_people = json.dumps(family)
print("turning dictionary to JSON...")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE






# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(family)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
print()

list_of_people = json.loads(json_people)
print(type(json_people))
print(type(family))

print(family)
for person in family:
    print(person['name'] + "," + person['occupation'] + "," + person['residence'] + "," + person['color'])