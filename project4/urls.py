"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application4 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('event',views.event,name="event"),
    path('about',views.about,name="about"),
    path('eventss',views.eventss,name="eventss"),
    path('privacy_policy',views.privacypolicy,name="privacypolicy"),
    path('faq',views.faq,name="faq"),
    path('eventadmin',views.eventadmin,name="eventadmin"),
    path('deletedata/<int:id>',views.deletedata),
    path('contact',views.contactform,name="contact"),
    path('contactadmin',views.contactadmin,name="contactadmin"),
    path('conference_and_seminars',views.cas,name="cas"),
    path('corprate_retreats',views.corprateretreats,name="corprateretreats"),
    path('product_launches',views.productlaunches,name="productlaunches"),
    path('award_ceremonies',views.awardceremonies,name="awardceremonies"),
    path('networking_events',views.networkingevents,name="networkingevents"),
    path('cpac',views.cpac,name="cpac"),
    path('wave',views.wave,name="wave"),
    path('contetn_development',views.contentdevelopment,name="contentdevelopment"),
    path('book_sound',views.booksound,name="booksound"),
    path('book_light',views.booklight,name="booklight"),
    path('led_display',views.leddisplay,name="leddisplay")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)