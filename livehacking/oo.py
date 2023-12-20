class Person:
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    @staticmethod
    def init_from_business_card(card_content):
        return Person(*card_content.split(' '))

    @property
    def firstname(self): return self._firstname
    @property
    def lastname(self): return self._lastname
    @lastname.setter
    def lastname(self, ln):
        if ln == 'Kickl':
            raise ValueError('geh weg')
        self._lastname = ln
    
    def fullname(self):
        return self.firstname + ' ' + self.lastname


caro = Person.init_from_business_card('Caro Faschingbauer')
print(caro.firstname)
print(caro.lastname)

joerg = Person('Joerg', 'Faschingbauer')
print(joerg.firstname)
print(joerg.lastname)

joerg.lastname = 'Huber'
