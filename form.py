from extra_fun.generator_id import id_generator

class Form:

    def __init__(self):
        self._id                 = id_generator()
        self._adoption_center    = None
        self._adopter            = None
        self._assessor           = None
        self._pet                = None
    
    # Id class
    @property
    def get_id(self):
        return self._id

    # Adoption center
    @property
    def adoption_center(self):
        return self._adoption_center
    
    @adoption_center.setter
    def adoption_center(self, value):
        self._adoption_center = value
    
    # Adopter
    @property
    def adopter(self):
        return self._adopter
    
    @adopter.setter
    def adopter(self, value):
        self._adopter = value

    # Assessor
    @property
    def assessor(self):
        return self._assessor
    
    @assessor.setter
    def assessor(self, value):
        self._assessor = value
    
    # Pet
    @property
    def pet(self):
        return self._pet
    
    @pet.setter
    def pet(self, value):
        self._pet = value
    
    # STR
    def __str__(self):
        adoption_center = self.adoption_center.name
        id_form         = self.get_id
        adopted_pet     = self.pet.name
        by_assessor =    self.assessor.username
        to_adopter      = self.adopter.username

        return f"""
        < {adoption_center} >
        {'*' * (len(adoption_center) + 4)}
        Form No. {id_form}.
        Pet's name: {adopted_pet}
        created by {by_assessor} to {to_adopter}
        """