from uuid import uuid4


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = uuid4()
    
    def __str__(self):
        return self.name

