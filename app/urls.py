from django.urls import path 
from app import views

urlpatterns = [
    path('',views.home , name='home'),
    path('login',views.login_user , name='login'),
    path('logout',views.logout_user , name='logout'),
    path('catageryview/<str:foo>', views.catageryview, name='catageryview'),
    path('subcatageryadd/<str:foo>',  views.subcatagery_add ,name='subcatageryadd'),
    path('deletecatagery/<int:pk>', views.delete_catagery , name='delete_catagery'), 
    path('deletesubcatagery/<int:pk>', views.delete_sub_catagery , name='delete_sub_catagery'),
    path('register', views.register.as_view(), name='register'),
    
]
