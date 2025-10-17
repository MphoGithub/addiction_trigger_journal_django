from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('view_triggers/', views.view_triggers, name='view_triggers'),
    path('add_trigger/', views.add_trigger, name='add_trigger'),
    path('edit_trigger/<int:trigger_id>/', views.edit_trigger, name='edit_trigger'),
    path('delete_trigger/<int:trigger_id>/', views.delete_trigger, name='delete_trigger'),
]
