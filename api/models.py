from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    dis = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.title


class Comment(models.Model):
    comments = models.CharField(max_length=500)
    post_id = models.ForeignKey(Blog,related_name='comment',on_delete=models.CASCADE)



class Like(models.Model):
    post_id = models.ForeignKey(Blog,related_name='like',on_delete=models.CASCADE)