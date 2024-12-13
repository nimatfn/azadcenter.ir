from django.db import models

from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):

        return self.name

class Customer(models.Model):

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    phone = models.CharField(max_length=11)

    email = models.EmailField(max_length=100)

    password = models.CharField(max_length=50)

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

class Product(models.Model):

    name = models.CharField(max_length=50)

    description = models.CharField(max_length=500, blank=True , null=True, default='')

    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)

    star= models.IntegerField(default=0 , validators=[MinValueValidator(0), MaxValueValidator(5)])

    picture = models.ImageField(upload_to="upload/products/")

    is_sale= models.BooleanField(default=False)

    sale_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):

        return self.name

class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    address=models.CharField(max_length=500 , blank=False)

    phone=models.CharField(max_length=11 , blank=True)

    date=models.DateField(default=timezone.now)

    status=models.BooleanField(default=False)    #یعنی در حال حاضر سفارش انجام نشده ، برای وضعیت دو حالت انجام شده و انجام نشده را درنظر گرفته ام

    def __str__(self):

        return self.product