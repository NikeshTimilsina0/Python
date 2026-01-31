test_settings={
    'theme':'light'
}

def add_setting(settings,new_item):
    key,value=new_item
    key=key.lower()
    value=value.lower()

    if key in settings:
        return "Setting 'theme' already exists! Cannot add a new setting with this name."
    settings[key]=value
    return "Setting 'volume' added with value 'high' successfully!"


def update_setting(settings,update_item):
    key,value=update_item
    key=key.lower()
    value=value.lower()

    if key not in settings:
        return "Setting 'volume' does not exist! Cannot update a non-existing setting."

    settings[key]=value
    return "Setting 'theme' updated to 'dark' successfully!"


def delete_setting(settings,key):
    key=key.lower()

    if key  in settings:
        del settings[key]
        return "Setting 'theme' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    # Check if dictionary is empty
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    
    
    for key, value in settings.items():
        
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"
    
    return result
    