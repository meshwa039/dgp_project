from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('category', views.category, name='category'),
    path('categoryedit', views.categoryedit, name='categoryedit'),
    path('feedback', views.feedback, name='feedback'),
    path('feedbackreport', views.feedbackreport, name='feedbackreport'),
    path('user', views.user, name='user'),
    path('userreport', views.userreport, name='userreport'),
    path('birth', views.birth, name='birth'),
    path('birthreport', views.birthreport, name='birthreport'),
    path('death', views.death, name='death'),
    path('deathreport', views.deathreport, name='deathreport'), 
    path('tax', views.tax, name='tax'),
    path('taxreport', views.taxreport, name='taxreport'),
    path('cast', views.cast, name='cast'),
    path('castreport', views.castreport, name='castreport'),
    path('income', views.income, name='income'),
    path('incomereport', views.incomereport, name='incomereport'),
    path('employee', views.employee, name='employee'),
    path('employeeedit', views.employeeedit, name='employeeedit'),
    path('employeereport', views.employeereport, name='employeereport'),
    path('village', views.village, name='village'), 
    path('villageedit', views.villageedit, name='villageedit'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('birthdetails', views.birthdetails, name='birthdetails'),
    path('castdetails', views.castdetails, name='castdetails'),
    path('deathdetails', views.deathdetails, name='deathdetails'),
    path('incomedetails', views.incomedetails, name='incomedetails'),
    path('taxdetails', views.taxdetails, name='taxdetails'),
    
]