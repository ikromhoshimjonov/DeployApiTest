from django.db.models import Model, CharField, ForeignKey, DecimalField, SET_NULL


class Categories(Model):
    name = CharField(max_length=255)

class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10,decimal_places=0)
    category = ForeignKey("apps.Categories",on_delete=SET_NULL,null=True,blank=True)