from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class TravelBlog(models.Model):
    place_name=models.CharField(max_length=100)
    district_name=models.CharField(max_length=100)
    country_name=models.CharField(max_length=100)
    about=models.TextField()
    description=models.TextField()
    image=CloudinaryField(null=True,blank=True)
    video_url=models.CharField(max_length=1000)
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.place_name +" "+ self.country_name

class TravelPlace(models.Model):
    place_name=models.CharField(max_length=100)
    district_name=models.CharField(max_length=100)
    country_name=models.CharField(max_length=100)
    image=CloudinaryField(null=True,blank=True)
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.place_name +" "+ self.country_name


class Food(models.Model):
    food_name=models.CharField(max_length=100)
    famous_in_city=models.CharField(max_length=100)
    famous_in_country=models.CharField(max_length=100)
    about=models.TextField()
    description=models.TextField()
    image=CloudinaryField(null=True,blank=True)
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.food_name +" "+ self.famous_in_country
class Drama(models.Model):
    drama_name=models.CharField(max_length=100)
    famous_in_country=models.CharField(max_length=100)
    about=models.TextField()
    description=models.TextField()
    image=CloudinaryField(null=True,blank=True)
    video_url=models.CharField(max_length=1000)
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.drama_name +" "+ self.famous_in_country


class About(models.Model):
    app_name=models.CharField(max_length=100)
    image=CloudinaryField(null=True,blank=True)
    about_us=models.TextField()
    privacy_policy=models.TextField()
    facebook=models.URLField(default='www.facebook.com')
    instagram=models.URLField(default='www.instagram.com')
    youtube=models.URLField(default='www.youtube.com')

    def __str__(self):
        return self.app_name