from django.db import models

# Create your models here. 
class Task(models.Model):
    task_details=models.TextField(max_length=50)
    task_type=models.CharField(max_length=50)
    def _str_(self):
        return str(self.task_details)
    
class User(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length=50)
    Mobile = models.IntegerField()
    ID = models.AutoField(primary_key=True)
    Task = models.ForeignKey(Task,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='User'
    def _str_(self):
        return self.Name
