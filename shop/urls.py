
from django.urls import path,include

from  .views import about, login_user,logout_user,home,signup_user,product,category,category_summary,update_user

urlpatterns = [

    path('',home, name='home'),

    path('about/',about , name='about'),

    path('login/', login_user , name='login'),

    path('logout/',logout_user , name='logout'),

    path('signup/',signup_user,name='signup'),

    path('product/<int:pk>',product,name='product'),

    path('category/<str:cat>/',category, name='category'),

    path('category/',category_summary, name='category_summary'),

    path('update_user/',update_user, name='update_user'),

]