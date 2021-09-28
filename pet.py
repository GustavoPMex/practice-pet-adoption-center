from extra_fun.generator_id import id_generator

class Pet:

    def __init__(self):
        self._id             = id_generator()
        self._name           = None
        self._classification = None
        self._weight         = None
        self._height         = None
        self._age            = None
        self._sex            = None
        self._color          = None
    
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

    # Classification
    @property
    def classification(self):
        return self._classification
    
    @classification.setter
    def classification(self, value):
        self._classification = value
    
    # Weight
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        self._weight = value
    
    # Height
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    # Age
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
    
    # Sex
    @property
    def sex(self):
        return self._sex
    
    @sex.setter
    def sex(self, value):
        self._sex = value
    
    # Color
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value