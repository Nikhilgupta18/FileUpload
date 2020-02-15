from django.urls import path

from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('login/',views.Login.as_view()),
    path('logout/',views.Logout.as_view()),
    # path('signup/',views.SignUp.as_view()),
    path('signup/', views.signup, name='signup'),
    path('upload_file/', views.upload_file, name='upload_file'),

]

