# Javascript object notation
import json
from urllib.request import urlopen

print('\nWorking with json strings', '-' * 100, '\n')

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "555-555-5555",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "333-333-3333",
            "emails": null,
            "has_license": true            
        }
    ]
}
'''

# When loading json into a python object it uses the following conversion table
# to do so. Json objects get converted to a Dict
# https://docs.python.org/3.6/library/json.html
print(
    'When loading json into a python object it uses the following conversion '
    'table to do so')
print('https://docs.python.org/3.6/library/json.html')
# The loads method will load a string and the load method will load a file
data = json.loads(people_string)
print(data)

for person in data['people']:
    print(person)
    print(person['name'])

print()
# Remove elements form the dictionary
for person in data['people']:
    del person['phone']
new_string = json.dumps(data)
print(new_string)
new_string = json.dumps(data, indent=2)
print(new_string)
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

print('\nWorking with json files', '-' * 100, '\n')

# load from a json file
with open('states.json') as f:
    # The loads method will load a string and the load method will load a file
    data = json.load(f)

for state in data['states']:
    print(state)

# load into a json file

for state in data['states']:
    del state['area_codes']
    print(state)

with open('new_states.json', 'w') as new_f:
    json.dump(data, new_f, indent=2)

print('\nWorking with json files from URL', '-' * 100, '\n')

with urlopen(
        "http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?"
        "format=json") as response:
    source = response.read()

print(source)

data = json.loads(source)
# print(json.dumps(data, indent=2))

print(len(data['list']['resources']))

for item in data['list']['resources']:
    print(item)

usd_rates = dict()
for item in data['list']['resources']:
    name = ''
    price = ''
    try:
        name = item['resource']['fields']['name']
        price = item['resource']['fields']['price']
        usd_rates[name] = price
    except KeyError as e:
        print('\nThe {} key was missing'.format(e))
    print(name, price)
print(usd_rates['USD/EUR'])
d = '$50 US would be worth: ' + '$' + (
    str(50 * float(usd_rates['USD/EUR']))) + ' in Euros'
print(d)
print()
