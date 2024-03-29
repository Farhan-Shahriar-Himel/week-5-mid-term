from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='carbrands/media/uploads')


    def __str__(self) -> str:
        return f"{self.brand} {self.name}"
    

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Commented by {self.name}"
