from faker import Faker

from .models import *
fake = Faker()

import random


def seed_db(n=10)->None:
    try:
            
         for i in range(0,n):
             department_obj = Department.objects.all()
             index = random.randint(0,len(department_obj)-1)

             department = department_obj[index]             
             student_id = f'STU-0{random.randint(100,999)}'
             
             student_name = fake.name()
             student_email= fake.email()
             student_age = random.randint(20,30)
             student_adress= fake.address()
     
             student_id_obj = StudentId.objects.create(student_id = student_id)
     
             student_obj = Student.objects.create(
     
             department = department,
             student_id = student_id_obj,
             student_name = student_name,
             student_email = student_email,
             student_age = student_age,
             student_adress = student_adress,
          
     
     
             )
    except Exception as e:
        print(e)
