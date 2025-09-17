from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_present = models.BooleanField(default=False)
    student_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.last_name}"
    

    
