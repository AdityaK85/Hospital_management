from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.signup),
    path('login/', views.login_),
    path('signup_handle/', views.signup_handle),
    path('login_handle/', views.user_login),
    path('logout_page/', views.logout_page),

    path('dashboard/', views.dashboard),
    path('hospital/', views.index),
    path('department/', views.department),
    path('doctor/', views.doctor),
    path('patient/', views.patient),
    path('appointment/', views.appointment),
    path('schedule/', views.schedule),
    path('manage_department/', views.manage_department),
    path('manage_doctor/', views.manage_doctor),
    path('manage_patients/', views.manage_patients),
    path('display_appointment/', views.display_appointment),
    path('display_schedule/', views.display_schedule),

    path('save_department/', views.save_department),
    path('save_doctor/', views.save_doctor),
    path('save_patient/', views.save_patient),
    path('save_appointment/', views.save_appointment),
    path('save_schedule/', views.save_schedule),

    path('delete_department/', views.delete_department),
    path('delete_doctor/', views.delete_doctor),
    path('delete_patient/', views.delete_patient),
    path('delete_appointment/', views.delete_appointment),
    path('delete_schedule/', views.delete_schedule),

    path('edit_department/<int:id>', views.edit_department),
    path('edit_doctor/<int:id>', views.edit_doctor),
    path('edit_patient/<int:id>', views.edit_patient),
    path('edit_appointment/<int:id>', views.edit_appointment),
    path('edit_schedule/<int:id>', views.edit_schedule),

    path('upader_department/', views.update_department),
    path('update_doctor/', views.update_doctor),
    path('update_patient/', views.update_patient),
    path('update_appointment/', views.update_appointment),
    path('update_schedule/', views.update_schedule),
]
