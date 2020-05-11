from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('deletefromcarthome/<int:id>', views.deletefromcarthome, name='deletefromcarthome'),
     # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),

]