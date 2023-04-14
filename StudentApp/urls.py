from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.home),
    path('addstudent',views.addstudent,name='addstudent'),
    path('display',views.display,name='display'),
    path('displaystudent',views.displaystudent,name='displaystudent'),
    path('updatedata/<int:id>',views.updatedata,name='updatedata'),
    path('deletedata/<int:id>',views.deletedata,name='deletedata')
]