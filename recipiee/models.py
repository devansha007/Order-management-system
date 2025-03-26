from django.db import models
from django.contrib.auth.models import User
                                                                             
# Create your models here.                                                                                                                                  

class Recipie(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,blank=True ,null=True)
    recipie_name=models.CharField(max_length=100)
    recipie_description=models.TextField()
    recipie_img=models.ImageField(upload_to= "recpie")
    recipie_view_count =models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.recipie_name
    
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department'] 


class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department = models.ForeignKey(Department ,related_name="depart",on_delete=models.CASCADE)    
    student_id = models.OneToOneField(StudentId , related_name="studentid",on_delete=models.CASCADE)
    student_name =models.CharField(max_length=100)
    student_email =models.EmailField(unique=True)
    student_age =models.IntegerField(default=18)
    student_adress =models.TextField()

    def __str__(self) -> str:
        return self.student_name
    

    class Meta:
        ordering = ['student_name']
        verbose_name ="student"