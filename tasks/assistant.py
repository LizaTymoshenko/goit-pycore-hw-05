from functools import wraps

# decorator
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Provide a name please."
        except KeyError:
            return "This contact does not exist."

    return inner

# functions
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        old_contact = contacts[name]
        return f"Contact already exists with number '{old_contact}'. If you want to change phone for this contact, use command 'change username new_phone'."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if not contacts.get(name):
        return "No such contact."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if len(args) > 1:
        print("Returning only 1 contact per comand.")
    phone = contacts[name]
    return phone

@input_error
def show_all(contacts):
    if not contacts:
        return "Contact book is empty."
    else:
        return "\n".join([": ".join((k,v)) for k, v in contacts.items()])

# assistant loop
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    commands_list = ("Please enter a valid ommand. "
                    "\nAvailable commands:"
                    "\n\t - add <username> <phone> "
                    "\n\t - change <username> <phone>"
                    "\n\t - phone <username>"
                    "\n\t - all "
                    "\n\t - close \\ exit.'")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print(commands_list)
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(commands_list)

if __name__ == "__main__":
    main()
