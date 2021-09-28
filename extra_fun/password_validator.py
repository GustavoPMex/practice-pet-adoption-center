
def validator(password):
    if len(password) <= 5:
        raise ValueError('Password length must be greater than 5')

    elif password[0].islower():
            raise ValueError('Password first letter must be capital letter')
        
    elif password.isalpha() or not password.isalnum():
        raise ValueError('Password must be alphanumeric')

    return password