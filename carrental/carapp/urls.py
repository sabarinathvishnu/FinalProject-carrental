from django.urls import path
from carapp import views

urlpatterns = [
   path('index/',views.index,name="index"),
   path('about/',views.aboutpage,name="about"),
   path('service/',views.servicepage,name="service"),
   path('car/',views.carpage,name="car"),
   path('contact/',views.contactpage,name="contact"),
   path('save_contact/',views.save_contact,name="save_contact"),
   path('cardetails/<int:cid>/',views.cardetails,name="cardetails"),
   path('booknow/<int:cid>/',views.booknow,name="booknow"),
   path('savebooknow/',views.savebooknow,name="savebooknow"),
   path('register/', views.register, name="register"),
   # path('save_register/',views.save_register,name="save_register"),
   path('userlogin/',views.userlogin,name="userlogin"),
   # path('userlogin_page/',views.userlogin_page,name="userlogin_page"),
   path('userlogout/', views.userlogout, name="userlogout"),
   path('bookingsdetail/', views.bookingsdetail, name="bookingsdetail"),
   path('login/',views.LoginView.as_view(),name='login'),
   path('logout/',views.log_out_view,name='logout'),
   # path('search_car/',views.search_car,name='search_car')


]