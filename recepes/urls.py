from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile_page, name="profile"),
    path('form', views.recepes_form, name="form"),
    path('detail/<int:pk>', views.detail_recepes, name="detail"),
    path('edit/<int:pk>', views.edit_recepes, name="edit"),
    path('delete/<int:pk>', views.delete_recepes, name="delete"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('send_email/', views.sendEmail, name="send_email"),
    path('search/', views.navbar_search_result, name="search"),

]



