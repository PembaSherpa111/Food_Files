import json

f = open('foods_info.json') #json file needs to be in same folder 
string_dictionary = f.read()
foods_info = json.loads(string_dictionary) 
f.close()

low_fat_count = 0
high_fiber_count = 0
low_glycemic_index_count = 0

for i in range(0,len(foods_info)):
    dict=foods_info[i]
    if (dict['low fat']).lower() == 'yes':
        low_fat_count += 1
    if (dict['high fiber']).lower() == 'yes':
        high_fiber_count += 1
    if (dict['low glycemic index']).lower() == 'yes':
        low_glycemic_index_count += 1

print(f'Number of low fat foods = {low_fat_count}, Number of high fiber foods = {high_fiber_count}, and Number of low glycemic index foods = {low_glycemic_index_count}')

print(f'''
Percentage of low fat foods = {(low_fat_count/len(foods_info))*100} %
Percentage of high fiber foods = {(high_fiber_count/len(foods_info))*100} %
Percentage of low glycemic index foods = {(low_glycemic_index_count/len(foods_info)*100)} %\n''')

for i in range(0,len(foods_info)):
    dict=foods_info[i]
    if (dict['low fat']).lower() == 'yes':
        if (dict['high fiber']).lower() == 'yes':
            if (dict['low glycemic index']).lower() == 'yes':
                print(f'{dict["foods"]} is recommended food.')
print(len(foods_info))