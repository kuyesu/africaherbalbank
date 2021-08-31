from django.db import models

# Create your models here.
class Subscribers(models.Model):
     
    """subscribers detail"""
    fullname = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)

    def __str__(self):
        return self.fullname
    
    
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"