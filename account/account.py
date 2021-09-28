from extra_fun.generator_id import id_generator
from extra_fun.password_validator import validator

class Account:

    def __init__(self):
        self._id            = id_generator() 
        self._username      = None
        self._password      = None
        self._documents     = None
        self._phone         = None
        self._email         = None
        self._authorization = None
    
    # Id class
    @property
    def get_id(self):
        return self._id
        
    # Username
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if value:
            if not value.isalpha():
                    raise ValueError('Username must be alphabetic e.g "newUser"')
            self._username = value
        else:
            raise ValueError('Empty values are not allowed')

    # Password
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if value:
            self._password = validator(value)
        else:
            raise ValueError('Empty values are not allowed')
    
    #  Documents
    @property
    def documents(self):
        return self._documents

    @documents.setter
    def documents(self, value):
        if value:
            self._documents = value
        else:
            raise ValueError('Empty values are not allowed')
    
    # Phone
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if value:
            if type(value) != int:
                raise ValueError('Phone must be integer')

            if len(str(value)) <= 5:
                raise ValueError('Phone must be greater than 5')

            self._phone = value
        else:
            raise ValueError('Empty values are not allowed')

    # Email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if value:
            if '@' not in value or '.com' not in value:
                raise ValueError('Enter a valid email')
            self._email = value
        else:
            raise ValueError('Empty values are not allowed')
    
    # Auth
    @property
    def authorization(self):
        return self._authorization
    
    @authorization.setter
    def authorization(self, value):
        self._authorization = value
