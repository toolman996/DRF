from django.urls import path

from ccokt import views

app_name='ccokt'
urlpatterns=[
    path('user/',views.user,name='user'),
    path('drf/',views.Drf.as_view()),
    path('drf/<str:id>/',views.Drf.as_view()),
    path('api/',views.UserApiView.as_view()),
]


