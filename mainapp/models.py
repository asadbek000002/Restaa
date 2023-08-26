from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    
class Meal(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    image = models.ImageField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    recipe = models.TextField(max_length=1000)
    real_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # valyuta turini aniqlash uchun

    # ovqatni posrsiyasi orqali bolimlarga ajratish

    SIZE_CHOICES = [(i, str(i)) for i in ['05_HISSA', 'ODATIY',]]
    porsiya = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True, null=True)

    MIQDOR_CHOICES = [(i, str(i)) for i in ['0.5 L', '1 L', '1.5 L', '2 L']]
    liter = models.CharField(choices=MIQDOR_CHOICES, max_length=10, blank=True, null=True)
    def get_created_time(self):
        return self.created.strftime('%D:%H')
    
    def __str__(self):
        return f'{self.name} | {self.porsiya}'






class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.meal.name

    @property
    def order_item_price(self):
            total = self.meal.price * Decimal(self.quantity)
            return total

    @property
    def order_item_total_price(self):
            total = self.meal.price * Decimal(self.quantity)
            return Decimal(total)


    @staticmethod
    def total_order_price():
        total_sum = Decimal('0')
        order_items = OrderItem.objects.all()
        for order_item in order_items:
            total_sum += order_item.order_item_total_price
        return f"{total_sum:.2f}"

    @staticmethod
    def total_quantity():
        t_quantity = Decimal('0')
        quantities = OrderItem.objects.all()
        for quantity in quantities:
            t_quantity += quantity.quantity
        return f"{t_quantity}"


