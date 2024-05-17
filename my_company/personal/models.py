from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=230 ,default="company")
    location = models.CharField(max_length=230 )
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    open_hour = models.CharField(max_length=30,blank=True,null=True)
    video_url = models.URLField(null=True)
    twitter_url =models.URLField(blank=True ,null=True)
    facebook_url =models.URLField(blank=True ,null=True)
    instagram_url =models.URLField(blank=True ,null=True)
    linkedin_url =models.URLField(blank=True,null=True)

    def _str_(self):
        return self.company_name
class Service(models.Model):
    icon =models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200,unique=True)
    description =models.TextField()
    
    def __str__(self):
        return self.title
    




class FrequentlyAskedQuestion(models.Model):
  question = models.CharField(max_length=255)
  answer = models.TextField()

  def __str__(self):
      return self.question

class TestimonialReview(models.Model):
    user_image = models.CharField(max_length=200)
    stars_count =[
       (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
         (5,'five'),
    ]
    rating_count = models.IntegerField(choices=stars_count)
    username = models.TextField()
    user_job_title= models.CharField(max_length=200)
    review = models.TextField()

def __str__(self):
      return f"{self.username} -{self.user_job_title}"


