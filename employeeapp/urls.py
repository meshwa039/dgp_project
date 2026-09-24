from django.urls import path

from . import views

urlpatterns = [
    path('', views.eindex,name='eindex'),
    path('ecategory', views.ecategory, name='ecategory'),
    path('ecategoryedit', views.ecategoryedit, name='ecategoryedit'),
    path('efeedback', views.efeedback, name='efeedback'),
    path('efeedbackreport', views.efeedbackreport, name='efeedbackreport'),
    path('euser', views.euser, name='euser'),
    path('euserreport', views.euserreport, name='euserreport'),
    path('ebirth', views.ebirth, name='ebirth'),
    path('ebirthreport', views.ebirthreport, name='ebirthreport'),
    path('edeath', views.edeath, name='edeath'),
    path('edeathreport', views.edeathreport, name='edeathreport'), 
    path('etax', views.etax, name='etax'),
    path('etaxedit', views.etaxedit, name='etaxedit'),
    path('etaxreport', views.etaxreport, name='etaxreport'),
    path('ecast', views.ecast, name='ecast'),
    path('ecastreport', views.ecastreport, name='ecastreport'),
    path('eincome', views.eincome, name='eincome'),
    path('eincomereport', views.eincomereport, name='eincomereport'),
    path('eemployee', views.eemployee, name='eemployee'),
    path('eprofile', views.eprofile, name='eprofile'),
    path('eemployeereport', views.eemployeereport, name='eemployeereport'),
    path('evillage', views.evillage, name='evillage'), 
    path('evillageedit', views.evillageedit, name='evillageedit'),
    path('elogin', views.elogin, name='elogin'),
    path('elogout', views.elogout, name='elogout'),
    path('ebirthdetails', views.ebirthdetails, name='ebirthdetails'),
    path('ecastdetails', views.ecastdetails, name='ecastdetails'),
    path('edeathdetails', views.edeathdetails, name='edeathdetails'),
    path('eincomedetails', views.eincomedetails, name='eincomedetails'),
    path('etaxdetails', views.etaxdetails, name='etaxdetails'),
    path('get_taluka/<str:district_name>/', views.get_taluka, name='get_taluka'),
    path('get_village/<str:taluka_name>/', views.get_village, name='get_village'),
    
]