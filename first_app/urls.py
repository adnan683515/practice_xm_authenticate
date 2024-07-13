
from django.urls import path
from . import views
urlpatterns = [
   path("registrationForm/",views.registrationForm,name='sign_up_page'),
   path("log_in/",views.log_in,name="log_in_page"),
   path("profile/",views.profile_page,name='Profile_page'),
   path("logOUt/",views.log_out,name="log_out_page"),
   path('passchange/',views.change_pass,name='change_pass'),
   path("passchange2/",views.pass_change_2,name='change_pass_2')
]
