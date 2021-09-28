from account.account import Account

class Assessor(Account):

    def __init__(self):
        super().__init__()
        self._access_key = None
    
    @property
    def access_key(self):
        return self._access_key
    
    @access_key.setter
    def access_key(self, value):
        self._access_key = value

        