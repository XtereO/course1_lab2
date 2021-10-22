
import csv

# Support function
def csv_to_list(file_name:str):
    
    list_objects = []
    keys = []
    with open(file_name, encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(keys)==0: keys.extend(row)
            else:
                new_object = {}
                for i in range(len(keys)):
                    new_object[keys[i]] = row[i]
                list_objects.append(new_object)

    return list_objects

def collect_all_props(list_objects,key):

    all_props = []
    for item in list_objects:
        if len(item[key].split(', '))>1:
            for subItem in item[key].split(', '):
                if not subItem in all_props:
                    all_props.append(subItem)        
        elif not item[key] in all_props:
            all_props.append(item[key])
    
    return all_props
                    
def require_params(get_information,action):
        
        value = input(f'Введите {title}' 
        +f'(Чтобы получить все {title} введите get):')
        
        if value == 'get':
            print(get_information())
            return require_params(get_information,title)
        else:
            return value.replace(' ','').split(',')