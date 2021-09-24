from django.db import models

# Create your models here.
class book(models.Model):
    def __str__(self): #if this method is removed then,
        #it will not not display book name,
 # it will display number of books
        return self.name

    name = models.CharField(max_length = 120)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField()
    bk_image = models.ImageField(default = 'default.jpg', upload_to = 'bookimage')