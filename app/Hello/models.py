from django.db import models as data_type


class User_list(data_type.Model):
    first_name=data_type.CharField(max_length=250)
    last_name=data_type.CharField(max_length=250)
    email=data_type.EmailField(unique=True)
    password=data_type.CharField(max_length=250)
    date_of_join=data_type.CharField(max_length=250)
    superuser=data_type.BooleanField(default=False)
    def __str__(self):
        return self.first_name+' '+self.last_name

class Attendance(data_type.Model):
    user=data_type.ForeignKey(User_list,on_delete=data_type.CASCADE)
    date=data_type.CharField(max_length=250)
    status=data_type.BooleanField(default=False)