#reading function
def reader(file_name):
    with open(f'{file_name}.txt','r') as str_file:
        list_file=[line.rstrip() for line in str_file]
    return(list_file)

# delete by index for all the list
def delete(idx):
    del foods_list[idx]
    del highfiber_list[idx]
    del lowfat_list[idx]
    del low_glycemic_index_list[idx]
    return(foods_list,highfiber_list,lowfat_list,low_glycemic_index_list)

import json
#cleaning missing data function
def clean_missing(file_list):
    for idx, val in enumerate(file_list):
        if val == '':
            delete(idx)
    return(foods_list,highfiber_list,lowfat_list,low_glycemic_index_list)

#creating key:value pair function
def dict_file(file_list):
    dict_file= []
    for i in range(1,len(file_list)):
        dict_file.append(f'{file_list[0]}:{file_list[i]}')
    return(dict_file)
    
#variables    
foods = 'foods'
highfiber = 'highfiber'
lowfat = 'lowfat'
low_glycemic_index = 'low-glycemic-index'

#Reading 
foods_list = reader(foods)
highfiber_list = reader(highfiber)
lowfat_list = reader(lowfat)
low_glycemic_index_list = reader(low_glycemic_index)
           
#cleaning dupliucate
file_set = set()
for idx, val in enumerate(foods_list):
    if val not in file_set:
        file_set.add(val)         
    else:
        delete(idx)

#cleaning missing data
clean_missing(foods_list)
clean_missing(highfiber_list)
clean_missing(lowfat_list)
clean_missing(low_glycemic_index_list)

#creating dictionary
foods_info = []

for i in range(1,len(foods_list)):
    foods_info.append({f"{foods_list[0]}":f"{foods_list[i]}",
                        f"{highfiber_list[0]}":f"{highfiber_list[i]}", 
                        f"{lowfat_list[0]}":f"{lowfat_list[i]}", 
                        f"{low_glycemic_index_list[0]}":f"{low_glycemic_index_list[i]}"})

with open("foods_info.json","w") as writer:
    json.dump(foods_info,writer)




