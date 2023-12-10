from django.urls import path,include
from .views import  *
urlpatterns = [
     
    path("",List),
    path("add/",post_List),
    path("update/<int:id>/",update_List),
    path("delete/<int:id>",delete_List),
    path("register/",ResgisterUser.as_view()),
]