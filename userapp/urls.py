from django.urls import path

from . import views

urlpatterns = [
    path('', views.uindex,name='uindex'),
    path('usignup', views.usignup,name='usignup'),
    path('usignin', views.usignin,name='usignin'),
    path('usignout', views.usignout,name='usignout'),
    path('uprofile', views.uprofile,name='uprofile'),
    path('uforgotpassword', views.uforgotpassword,name='uforgotpassword'),
    path('uabout', views.uabout,name='uabout'),
    path('ucontact', views.ucontact,name='ucontact'),
    path('uservice', views.uservice,name='uservice'),
    path('uterms', views.uterms,name='uterms'),
    path('ubirth', views.ubirth,name='ubirth'),
    path('ubirthview',views.ubirthview,name='ubirthview'),
    path('ubirthedit',views.ubirthedit,name='ubirthedit'),
    path('ubirthcertificate', views.ubirthcertificate,name='ubirthcertificate'),
    path('udeath', views.udeath,name='udeath'),
    path('udeathedit',views.udeathedit,name='udeathedit'),
    path('udeathview', views.udeathview,name='udeathview'),
    path('ucaste', views.ucaste,name='ucaste'),
    path('ucasteedit', views.ucasteedit,name='ucasteedit'),
    path('ucasteview', views.ucasteview,name='ucasteview'),
    path('uincome', views.uincome,name='uincome'),
    path('uincomeedit', views.uincomeedit,name='uincomeedit'),
    path('uincomeview', views.uincomeview,name='uincomeview'),
    path('get_taluka/<str:district_name>/', views.get_taluka, name='get_taluka'),
    path('get_village/<str:taluka_name>/', views.get_village, name='get_village'),
    path('check-password', views.check_password, name='check_password'),
    path('udeathcertificate', views.udeathcertificate,name='udeathcertificate'),
    path('ucastecertificate', views.ucastecertificate,name='ucastecertificate'),
    path('uincomecertificate', views.uincomecertificate,name='uincomecertificate'),
    path('utaxview', views.utaxview,name='utaxview'),
    path('utaxcertificate', views.utaxcertificate,name='utaxcertificate'),
    
]