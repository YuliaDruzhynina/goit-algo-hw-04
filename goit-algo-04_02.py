from pathlib import Path

def get_cats_info(path):
    result_dict = []

    try:
        with open(path) as file:
            file_text = file.readlines()
            
            for line in file_text:              
                id, name, age = line.strip().split(',')                                         
                cats_info = {'id': id,'name': name,'age': age}
                result_dict.append(cats_info)

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Unexpected result")

    return result_dict

cats_info = get_cats_info(r"path/to/cats_file.txt")  
print(cats_info)                           
