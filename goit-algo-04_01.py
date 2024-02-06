import re
from pathlib import Path

def total_salary(path):
    try:
        with open(path) as file:          
            file_text = str(file.readlines())                   
            #salary = []
            pattern = r"\d+"
            salary = re.findall(pattern, file_text)                                                                       
            salary_int = [int(num) for num in salary]
            total = sum(salary_int)                           
            average = int(total/ len(salary_int)) if len(salary_int) > 0 else 0                      

    except FileNotFoundError:       
        print('file not found')
    except Exception as e:
         return None
    return (total, average)                        


total, average = total_salary(r"path/to/salary_file.txt")

# if total is not None and average is not None:
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# else:
#     print("Error occurred.")

