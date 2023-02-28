from django.urls import path

from .views import *

app_name = 'app_education'
urlpatterns = [
    path('high_school/create/', HighSchoolCreateView.as_view(), name='education_high_school_create'),
    path('high_school/detail_update/', HighSchoolDetailUpdateView.as_view(), name='education_high_school_detail_update'),

    path('bachelor_degree/create/', BachelorDegreeCreateView.as_view(), name='education_bachelor_degree_create'),
    path('bachelor_degree/detail_update/', BachelorDegreeDetailUpdateView.as_view(), name='education_bachelor_degree_detail_update'),
]
