from django.urls import path
from .views import reader_list, ReaderCreate, ReaderEdit, ReaderDelete

urlpatterns = [
    path('', reader_list, name='reader_list'),
    path('create/', ReaderCreate.as_view(), name='reader_create'),
    path('update/<int:pk>/', ReaderEdit.as_view(), name='reader_update'),
    path('delete/<int:pk>/', ReaderDelete.as_view(), name='reader_delete'),
]
