from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+ ' '+self.email

class Person(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    postalcode = models.CharField(max_length=20)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.fname + ' '+self.lname

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=20)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(Person, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Person.fname + " by " + self.post.title




class Like(models.Model):
    sno= models.AutoField(primary_key=True)
    user=models.ForeignKey(Person, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user + " by " + self.post.title

