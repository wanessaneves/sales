from src.models.customer import Customer
from src.models.product import Product
from src.models.sale import Sale


c1 = Customer('Teste', 'teste@gmail.com')

p1 = Product('pão', 5.0)
p2 = Product('chá', 2.0)

products = [p1, p2]
v1 = Sale(c1, products)

print(v1.get_total())

