import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# -- TODO figure out the correct credential call here --
cred = credentials.Certificate("REMOVED FOR SECURITY")
firebase_admin.initialize_app(cred, {
    "projectId": "menu-1dbeb",
})

db = firestore.client()

# Menu
def menu():
    """Prints a menu to the terminal for the user to interact with
    No parameters, returns an INT"""
    print("\nSelect from the following:")
    print("1. Add Item")
    print("2. Check All Items")
    print("3. Delete Item")
    print("4. End\n\n")
    
    # See where the user wants to go next
    return int(input())

def add_item():
    """Attempts to add new word. If word exists in database 
    display error messsage. Otherwise add word. No arguments,
    returns nothing"""

    # Get user input to be stored in the database
    item = input("Name: ")
    definition = input(f'What is the definition of {item}? ')
    price = input("Price: ")

    # Check the collection to see if the item is in it.
    result = db.collection("menu").document(item).get()
    if result.exists:
        print("That word has already been stored.")
        return
    # else:
    data = {
        "word" : item,
        "defintion" : definition,
        "price" : price
    }
    
    db.collection("menu").document(item).set(data)

def check_all_items():


    print("Select From the Following:")
    print("1) Show All Inventory")        
    choice = input("")
    print()


    if choice == "1":
        menu_items = db.collection("menu").stream()
    else:
        print("Invalid Selection")
        return
    
    for item in menu_items:
        print(f"{item.id} => {item.to_dict()}")
    print() 

def delete_item():
    print("this currently does't work and will probably throw an error after this message ---")
    to_del = input("Name of item to delete: ")

    # Get all items to check if the item to delete exists before being removed.
    items = db.collection("menu").stream()

    if to_del in items:
        pass
        


def main():

    # Boundaries for user until quit is selected
    done = False
    while not done:
        user_selection = menu()
        
        if user_selection == 1:
            add_item()

        elif user_selection == 2:
            check_all_items()

        elif user_selection == 3:
            delete_item()
        
        elif user_selection == 4:
            done = True
            "Thank you for using our Cloud Service Menu System"

        # Error handling if user enters a bad input
        else:
            print('Please select a number within 1-4')


main()
