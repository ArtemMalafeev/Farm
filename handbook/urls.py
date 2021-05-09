from django.urls import path

from handbook.views import FertilizerDetail, FertilizerView, PestDetail, PestView

app_name = 'handbook'

urlpatterns = [
    path('pests/', PestView.as_view(), name='pest_list'),
    path('pests/<slug:slug>/', PestDetail.as_view(), name='pest_detail'),
    path('<slug:slug>/', FertilizerDetail.as_view(), name='fertilizer_detail'),
    path('', FertilizerView.as_view(), name='fertilizer_list'),
]
