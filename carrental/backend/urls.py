from django.urls import path
from backend import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:editid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:updateid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:deleid>/', views.deletecategory, name="deletecategory"),
    path('savevehicle/', views.savevehicle, name="savevehicle"),
    path('addvehicles/',views.addvehicles,name="addvehicles"),
    path('displayvehicles/',views.displayvehicles,name="displayvehicles"),
    path('editvehicle/<int:editid>/', views.editvehicle, name="editvehicle"),
    path('updatevehicle/<int:updateid>/', views.updatevehicle, name="updatevehicle"),
    path('deletevehicle/<int:deleid>/', views.deletevehicle, name="deletevehicle"),
    path('messages/', views.messages, name="messages"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),


    path('deletemesage/<int:deleid>/', views.deletemesage, name="deletemesage"),
    path('displaycustomers/', views.displaycustomers, name="displaycustomers"),
    path('deletecustomermessage/<int:deleid>/', views.deletecustomermessage, name="deletecustomermessage"),

]