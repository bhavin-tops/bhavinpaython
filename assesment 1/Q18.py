#Remove option must ask to user for ID to delete and again ask for confirmation
#(Y/N) before deletion and display proper message after deletion
def remove_option(id_list):
    id_to_remove = input("Enter ID to remove: ")
    if id_to_remove not in id_list:
        print("ID not found.")
        return
    
    confirm = input("Are you sure you want to remove ID {}? (Y/N) ".format(id_to_remove))
    if confirm.lower() != "y":
        print("Deletion cancelled.")
        return
    
    id_list.remove(id_to_remove)
    print("ID {} removed.".format(id_to_remove))

    id_list = ["bhavin", "chirag", "chiku"]
    remove_option(id_list)
