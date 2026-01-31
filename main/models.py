from django.db import models
from users.models import CustomUser



class CodeFile(models.Model):
    title= models.CharField(max_length=50,default='no title')
    file=models.FileField(upload_to='/files')
    dev=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}, {self.dev}"