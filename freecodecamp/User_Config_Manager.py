test_settings={"gamma":"high"}


def add_setting(dict_1, tuple_1):
    tuple_1 = (tuple_1[0].lower(), tuple_1[1].lower())
    if dict_1.get(tuple_1[0]) == None:
        dict_1.update([tuple_1])

        return f"Setting \'{tuple_1[0]}\' added with value \'{tuple_1[1]}\' successfully!"
    else:
        return f"Setting \'{tuple_1[0]}\' already exists! Cannot add a new setting with this name."



def update_setting(dict_1, tuple_1):
    tuple_1 = (tuple_1[0].lower(), tuple_1[1].lower())
    if  dict_1.get(tuple_1[0]) != None:
        dict_1.update([tuple_1])
        return f"Setting \'{tuple_1[0]}\' updated to \'{tuple_1[1]}\' successfully!"
    else:
        return f"Setting \'{tuple_1[0]}\' does not exist! Cannot update a non-existing setting."
    
def delete_setting(dict_1, key_1):
    key_1 = key_1.lower()
    if dict_1.get(key_1) != None:
        dict_1.pop(key_1)
        return f"Setting \'{key_1}\' deleted successfully"
    else:
        return f"Setting not found!"

def view_setting(dict_1):
    if not dict_1:
        return "No settings available."
    else:
        display_settings = ("Current User Settings:""\n")
        for x,y in dict_1.items():
            setting = f"{x.capitalize()}: {y}" + "\n"
            display_settings+=setting
        return display_settings




