import json

# open in read mode
json_file = open('cs109_module6_examples_data.json')

python_dictionary = json.load(json_file)

json_file.close()

new_name = 'David'
new_age = 16
new_city = 'Mississauga'

# loop through data to edit them
for k, v in python_dictionary.items():
    print(f'\nkey: {k} - value: {v}')
    if k == 'name':
        print(f'changing name {v} to {new_name}')
        python_dictionary[k] = new_name
    if k == 'age':
        print(f'changing age {v} to {new_age}')
        python_dictionary[k] = new_age
    if k == 'city':
        print(f'changing city {v} to {new_city}')
        python_dictionary[k] = new_city

# production
# json_string = json.dumps(python_dictionary)

# development
json_string = json.dumps(python_dictionary, indent = 2)
print('\nnew data:')
print(json_string)

# open in write mode
json_file = open('cs109_module6_examples_data.json', 'w')

json_file.write(json_string)

json_file.close()