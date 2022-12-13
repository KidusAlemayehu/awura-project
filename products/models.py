from django.db import models

# Create your models here.
def directory_path(instance, filename):
    return 'product-{0}/{1}/{2}'.format(instance.name,instance.model, filename)
# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "Products"
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    spec = models.CharField(max_length=50)
    price = models.FloatField()
    main_image = models.FileField(upload_to=directory_path, default=None)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)