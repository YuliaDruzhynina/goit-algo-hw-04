import re
from pathlib import Path

def total_salary(path):
    try:
        with open(path) as file:          
            file_text = file.read() 
            print(file_text)

        pattern = r"\d+"
        salary = re.findall(pattern, file_text)    
        salary_int = list(map(int, salary)) 
        total = sum(salary_int)                      
        average = int(total/ len(salary_int)) if len(salary_int) > 0 else 0                    

    except FileNotFoundError:       
        print('file not found')
        #return None, None
    except Exception as e:
         return None, None
    
    return total, average                        


total, average = total_salary(r"/Users/juliia/Desktop/GoIt_hw/Text-04_01.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# if total is not None and average is not None:

#     print("Error occurred.")

