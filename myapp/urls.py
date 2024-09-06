from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('logout_confirm/', views.logout_confirm_view, name='logout_confirm'),
    path('logout/', views.logout_view, name='logout'),
    path('add-time-slot/', views.add_time_slot, name='add_time_slot'),
    path('time_slot_list/', views.time_slot_list, name='time_slot_list'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_success/',views.appointment_success, name='appointment_success' ),
    path('manage_appointments/',views.manage_appointments, name='manage_appointments' ),
    path('notifications/',views.notifications, name='notifications' ),

   ]
