from django.urls import path

from .views import *

app_name = 'app_education'
urlpatterns = [
    path('high_school/create/', HighSchoolCreateView.as_view(), name='education_high_school_create'),
    path('high_school/detail_update/', HighSchoolDetailUpdateView.as_view(), name='education_high_school_detail_update'),

    path('bachelor_degree/create/', BachelorDegreeCreateView.as_view(), name='education_bachelor_degree_create'),
    path('bachelor_degree/detail_update/', BachelorDegreeDetailUpdateView.as_view(), name='education_bachelor_degree_detail_update'),

    path('master_degree/create/', MasterDegreeCreateView.as_view(), name='education_master_degree_create'),
    path('master_degree/detail_update/', MasterDegreeDetailUpdateView.as_view(), name='education_master_degree_detail_update'),

    path('program_request/create/', ProgramRequestedCreateView.as_view(), name='education_program_requested_create'),
    path('program_request/detail_update/<str:tracking_id>/', ProgramRequestedDetailUpdateView.as_view(), name='education_program_requested_detail_update'),
]
