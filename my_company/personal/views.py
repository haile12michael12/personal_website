from django.shortcuts import render,redirect
from django.http import HttpResponse
from personal.models import GeneralInfo,Service,FrequentlyAskedQuestion,TestimonialReview
from django.db import connection


# Create your views here.

def index(request):
  general_info = GeneralInfo.objects.first()

  services = Service.objects.all()
  faqs = FrequentlyAskedQuestion.objects.all()
  testimonialreview =testimonialreview.objects.all()
  context = {
    "company_name" :general_info.company_name,
    "location" :general_info.location,
    "email" :general_info.email,
    "phone" :general_info.phone,
    "open_hours" :general_info.open_hour,
    "video_url" :general_info.video_url,
    "twitter_url":general_info.twitter_url,
    "facebook_url":general_info.facebook_url,
    "instagram_url":general_info.instagram_url,
    "linkedin_url":general_info.linkedin_url,

    "services":services,
    
    "faqs":faqs,
    "testimonialreview":testimonialreview,
  }
  return render(request, "index.html", context)


def contact_form(request):
   if request.method =="POST":
    print("\nuser submit contact_form\n")
    print(f"request.POST : {request.POST}")
   return redirect('home')