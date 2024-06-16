from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from django.core.mail import send_mail

from django.conf import settings

from django.template.loader import render_to_string

from tana_software_solution.models import GeneralInfo,Service,FrequentlyAskedQuestion,Testimonial,Blog

from django.db import connection




# Create your views here.


def index(request):

  general_info = GeneralInfo.objects.first()


  services = Service.objects.all()

  faqs = FrequentlyAskedQuestion.objects.all()


  testimonials =Testimonial.objects.all()

  recent_blogs =Blog.objects.all().order_by("-created_at")[:3]

  #for blog in recents:

   #print(f"blog: {blog}")

   #print(f"blog.created_at:{blog.created_at}")

   #print(f"blog.author:{blog.author}")

   #print(f"blog.author.country:{blog.author.country}")

   #print("")

  default_value =""
  context = {

    "company_name" :getattr(general_info, "company_name",default_value),
    "location" :getattr(general_info,"location",default_value),
    "email" :getattr(general_info,"email",default_value),

    "phone" :getattr(general_info,"phone",default_value),

    "open_hours" :getattr(general_info,"open_hour",default_value),

    "video_url" :getattr(general_info,"video_url",default_value),

    "twitter_url":getattr(general_info,"twitter_url",default_value),

    "facebook_url":getattr(general_info,"facebook_url",default_value),
    "instagram_url":getattr(general_info,"instagram_url",default_value),

    "linkedin_url":getattr(general_info,"linkedin_url",default_value),


    "services":services,
    

    "faqs":faqs,
   
    "testimonials":testimonials,
    "recent_blogs":recent_blogs,

  }

  return render(request, "index.html", context)



def contact_form(request):

   if request.method =="POST":

    print("\nuser submit contact_form\n")

    name =request.POST.get("name")

    email =request.POST.get("email")

    subject=request.POST.get("subject")

    message=request.POST.get("message")

   context={
     "name":name,
     "email":email,

     "subject":subject,
     "message":message,

   }

   html_content=render_to_string('email.html',context)
   
   send_mail(

    subject=subject,

    message=None,

    html_message=html_content,

    from_email =settings.EMAIL_HOST_USER,

    recipient_list =[settings.EMAIL_HOST_USER],

    fail_silently=False,
    )
     

   return redirect('home')
   

def blog_details(request,blog_id):

  blog =Blog.objects.get(id=blog_id)

  recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]

  context={
    "blog":blog,
    "recent_blogs":recent_blogs,

  }

  return render(request,"blog_details.html",context)

def blogs(request):

  all_blogs =Blog.objects.all()

  blogs_per_page =3

  paginator = Paginator(all_blogs,blogs_per_page)

  print(f"paginator.num_pages :{paginator.num_pages} ")


  page =request.GET.get('page')

  print(f"page :{page}")

  try:
    blogs = paginator.page(page)

  except PageNotAnInteger:

    blogs = paginator.page(1)

  except EmptyPage:
   blogs =paginator.page(paginator.num_pages)

  context={
    "blogs":blogs,

  }

  return render(request,"blogs.html",context)