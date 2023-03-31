from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #adds date and time when object is created
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}") #returns only first and last name when called
