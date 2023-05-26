from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reminder_RestApi import views
from django.urls import path, include


urlpatterns = [
    

    path('reminder_RestApi/', views. Reminder_RestApiList.as_view()),
    path('reminder_RestApi/<int:pk>/', views.Reminder_RestApiDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)