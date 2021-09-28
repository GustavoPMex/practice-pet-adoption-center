from account.adopter import Adopter
from account.assessor import Assessor
from pet import Pet
from adoption_center import AdoptionCenter
from form import Form

def inProcess():
    # Only the Account class has validations
    new_adopter = Adopter()
    new_adopter.username    = 'newuser'
    new_adopter.password    = 'M123456'
    new_adopter.documents   = 'NADOC'
    new_adopter.phone       = 999996
    new_adopter.email       = 'new_adopter@g.com'
    new_adopter.authorization = False

    new_assessor = Assessor()
    new_assessor.username      = 'newassessor'
    new_assessor.password      = 'R098765'
    new_assessor.documents     = 'NADOC'
    new_assessor.phone         = 888886
    new_assessor.email         = 'new_assessor@g.com'
    new_assessor.authorization = True
    new_assessor.access_key    = 'ACCESS123'

    new_pet = Pet()
    new_pet.name           = 'New Pet'
    new_pet.classification = 'dog'
    new_pet.weight         = 6
    new_pet.height         = 60
    new_pet.age            = 3
    new_pet.sex            = 'male'
    new_pet.color          = 'white with brown'

    new_adoptionC = AdoptionCenter()
    new_adoptionC.name      = 'New Adoption Center: Pet Adoption Center'
    new_adoptionC.address   = 'Street 431 '
    new_adoptionC.phone     = 77777
    new_adoptionC.email     = 'mayrin@g.com'

    new_form = Form()
    new_form.adoption_center    = new_adoptionC
    new_form.adopter            = new_adopter
    new_form.assessor           = new_assessor
    new_form.pet                = new_pet

    print(new_form)
    

if __name__ == '__main__':
    inProcess()