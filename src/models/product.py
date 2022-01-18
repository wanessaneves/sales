from uuid import uuid4


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = uuid4()
    
    def __str__(self):
        return self.name
        
    
        
    