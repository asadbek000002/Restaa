from django.db import models




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








