from django.urls import path
from .views import *

app_name = 'food'
urlpatterns = [
    path('', index, name='index'),
    path('item/', item, name='item'),
    path('<int:item_id>/', detail, name='detail'),
    path('add', create_item, name='create_item'),
    path('update/<int:id>', update_item, name='update_item'),
    path('delete/<int:id>', delete_item, name='delete_item')
]
