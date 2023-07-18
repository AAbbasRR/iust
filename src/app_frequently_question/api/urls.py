from django.urls import path

from .views import *

app_name = 'app_frequently_question'
urlpatterns = [
    path('list/', FrequentlyQuestionView.as_view(), name='frequently_question_list'),
]
