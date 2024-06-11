from django.db import models

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    testimonial = models.TextField()
    logo = models.ImageField(upload_to='testimonials_logos/')

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    features = models.TextField()

class CaseStudy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)

class JobOpening(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

class CompanyInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    map_url = models.URLField()
