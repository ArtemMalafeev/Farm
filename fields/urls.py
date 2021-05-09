from django.urls import path

from fields import views
from fields.views import export_work_docx , FieldCreateView , FieldDetail , FieldEditView , FieldsView , job_add_view , \
    JobsDetail

app_name = 'fields'

urlpatterns = [
    path('add/', FieldCreateView.as_view(), name='add_field'),
    path('work/export/<slug:pk>/', export_work_docx, name='export_work'),
    path('work/add/', job_add_view, name='work_add'),
    path('work/<slug:pk>/', JobsDetail.as_view(), name='work_detail'),
    path('edit/<slug:slug>/', FieldEditView.as_view(), name='edit_field'),
    path('', FieldsView.as_view(), name='field_list'),
    path('<slug:slug>/', FieldDetail.as_view(), name='field_detail'),
    # path('crops/', CropView.as_view(), name='crop_list')
]
