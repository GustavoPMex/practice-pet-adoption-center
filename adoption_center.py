from extra_fun.generator_id import id_generator

class AdoptionCenter:

    def __init__(self):
        self.id = id_generator()
        self._name       = None
        self._address    = None
        self._phone      = None
        self._email      = None

    # Id class
    @property
    def get_id(self):
        return self._id
        
    # Name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    # Address
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value
    
    # Phone
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value
    
    # Email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value