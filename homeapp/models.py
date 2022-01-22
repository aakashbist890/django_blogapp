from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            outputsize=(300, 300)
            img.thumbnail(outputsize)
            img.save(self.image.path)

