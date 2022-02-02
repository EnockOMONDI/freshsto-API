from django.db import models
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from shop.models import Product
from account.models import Client

COUNTY_CATEGORY_TYPES = (
('Nairobi', 'Nairobi'),
('Lesotho', 'Lesotho'),
('Liberia', 'Liberia'),
('Libya', 'Libya'),
('Madagascar', 'Madagascar'),
('Malawi', 'Malawi'),
('Mali', 'Mali'),
('Mauritania', 'Mauritania'),
('Mauritius', 'Mauritius'),
('Morocco', 'Morocco'),
('Mozambique', 'Mozambique'),

)
TOWN_CATEGORY_TYPES = (
('Utawala','Utawala'),
('Niger', 'Niger'),
('Nigeria', 'Nigeria'),
('Rwanda', 'Rwanda'),
('Sao Tome and Principe', 'Sao Tome and Principe'),
('Senegal', 'Senegal'),
('Seychelles', 'Seychelles'),
('Sierra Leone', 'Sierra Leone'),
('Somalia', 'Somalia'),
('South Africa', 'South Africa'),
('South Sudan', 'South Sudan'),
('Sudan', 'Sudan'),
('Tanzania', 'Tanzania'),
('Togo', 'Togo'),
('Tunisia', 'Tunisia'),
('Uganda', 'Uganda' ),
('Zambia', 'Zambia' )
)
class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    house_number = models.CharField(max_length=150)
    street_name = models.CharField(max_length=150)
    area = models.CharField(max_length=127, choices=TOWN_CATEGORY_TYPES ,  blank=True,null=True,  default='Utawala')
    location =  models.CharField(max_length=127, choices=COUNTY_CATEGORY_TYPES,  blank=True,null=True,  default='Nairobi')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=30)
          
    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total=sum(item.get_cost() for item in self.items.all()) 
        return (float(total)-self.discount)

    def get_discount(self, client):
        total = float(self.get_total_cost())
        if client.has_discount:
            if client.no_of_orders == 1:
                self.discount = total * 0.1
                print(self.discount)
                return self.discount
            elif client.no_of_orders > 3 and client.no_of_orders < 5:
                self.discount = total * 0.25
                print(self.discount)
                return self.discount
            else:
                self.discount = total * 0.40
                return self.discount
        else:
            return self.discount == 0

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
