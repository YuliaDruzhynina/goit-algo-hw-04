import re
from pathlib import Path

def total_salary(path):
    try:
        with open(path) as file:
            file_text = file.readlines()            #read file return list
            pattern = r"\d+"
            salary = re.findall(pattern, file_text) #return list                                                    #print(salary)
            total = sum(salary)                    #return int
            avarage = total/ len(salary)           

    except FileNotFoundError:       
       
        return (total, avarage)       

total, average = total_salary(r"path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
