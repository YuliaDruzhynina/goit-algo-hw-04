def parse_input(user_input):
    cmd, *args = user_input.split()         #команда, данные
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if args[0] in contacts:
        add_contact(args, contacts)
    else:        
        return "Contact updated." 

def show_phone(args,contacts):
    name = args[0]
    return contacts[name]

def show_all(args,contacts):
    all_contact=''
    for key in contacts:
        all_contact+=f"{key} : {contacts[key]}\n"
    return all_contact  

def main():
    contacts = {'John':"123", 'Jane':"234", 'Steve':"555"}  #    [{'name':'John Doe', 'phone':'+380988858880'},
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":  
            print(add_contact(args, contacts))

        elif command == "show":  
          print (show_phone(args, contacts))

        elif command == "all":  
            print(show_all(args, contacts))

        else:
            print("Invalid command.")       
         

if __name__ == "__main__":
    main()
