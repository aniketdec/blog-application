from PIL import Image
from django.db import models
from django.contrib.auth.models import User
#from django.core.files.base import ContentFile
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class friend(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User,related_name='owner',null=True,on_delete=models.CASCADE)
    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.add(new_friend)
    def lose_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.remove(new_friend)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    email_id=models.EmailField(null=True)
    #follows = models.ManyToManyField('self', related_name='follow', symmetrical=False,blank=True)
    image=models.ImageField(default='profile.PNG',upload_to='profile_pics/',null=True)
    avatar=models.ImageField(default='avatar.PNG',upload_to='temp/')
    about_me=models.TextField(null=True)#image=models.ImageField(upload_to='temp')
    def save(self,**kwargs):
        super().save()
        img = Image.open(self.image.path)
        avt=img.copy()
        print (img)
        img=img.resize((300,300),Image.ANTIALIAS)    
        img.save(self.image.path)
        avt=avt.resize((40,40),Image.ANTIALIAS)
        avt.save(self.avatar.path)
    def __str__(self):
        return self.user.username
