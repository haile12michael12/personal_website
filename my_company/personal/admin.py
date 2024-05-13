from django.contrib import admin
from personal.models import (
 GeneralInfo, 
 Service,
 FrequentlyAskedQuestion,
 Testimonial
)

# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
  list_display =[
    "company_name",
     "location",
     "email",
     "phone",
     "open_hour",
]

randomly_fields = [
    "email",
]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display =[
     "title",
     "description",
]

search_fields = [
    "title",
]

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display =[
     "question",
     "answer",
]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display =[
     "username",
     "user_job_title",
     "rating_count",
]

def display_rating_count(self,object):
    return '*' * obj.rating_count
display_rating_count_short_description ="rating"

search_fields = [
    "title",
]