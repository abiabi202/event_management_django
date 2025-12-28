from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import data
from .models import contact
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')

def event(request):
    if request.method=='POST':
            name=request.POST['Name']
            phone=request.POST['phone']
            email=request.POST['email']
            date=request.POST['date']
            place=request.POST['place']
            event=request.POST['event']
            image=request.FILES.get('Image')
            doc=request.FILES.get('Doc')

            a='abiswaran14@gmail.com'
            c='your recent booking for events'
            d='we will contact you soon'

            send_mail(c,d,a,[email])

            obj=data()
            obj.name=name
            obj.phone=phone
            obj.email=email
            obj.date=date
            obj.place=place
            obj.event=event
            obj.image=image
            obj.doc=doc
            obj.save()
            messages.success(request, "We will contact you soon.")
            return redirect('event')
    a=data.objects.all()
   
    return render(request,'event.html',{'data':a})

def about(request):
     return render(request,'about.html')

def eventss(request):
     return render(request,'eventss.html')

def privacypolicy(request):
     return render(request,'privacy_policy.html')

def faq(request):
     return render(request,'faq.html')


def eventadmin(request):
     a=data.objects.all()
     return render(request,'eventadmin.html',{'data':a}) 

def deletedata(request,id):
     a=data.objects.get(id=id)
     a.delete()
     return redirect('eventadmin')

def contactform(request):
    if request.method == "POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            phone=request.POST['phone']
            email=request.POST['email']
            message=request.POST['message']

            a='abiswaran14@gmail.com'
            c='your recent booking for contact'
            d='we will contact you soon'

            send_mail(c,d,a,[email])


            objects=contact()
            objects.fname=fname
            objects.lname=lname
            objects.phone=phone
            objects.email=email
            objects.message=message
            objects.save()

            messages.success(request, "We will contact you soon.")
            
            return redirect('contact') 
    return render(request, 'contact.html')

def contactadmin(request):
     a=contact.objects.all()
     return render(request,'contactadmin.html',{'data':a})

def cas(request):
     return render(request,'cas.html')

def corprateretreats(request):
    return render(request,'corprate_retreats.html')

def productlaunches(request):
    return render(request,'product_launches.html')

def awardceremonies(request):
    return render(request,'award_ceremonies.html')

def networkingevents(request):
    return render(request,'networking_events.html')

def cpac(request):
    return render(request,'cpac.html')

def wave(request):
    return render(request,'wave.html')

def contentdevelopment(request):
    return render(request,'content_development.html')

def booksound(request):
    return render(request,'book_sound.html')

def booklight(request):
    return render(request,'book_light.html')

def leddisplay(request):
    return render(request,'led_display.html')

