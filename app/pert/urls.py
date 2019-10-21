from django.contrib import admin
from django.urls import path
from Hello import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/',views.createuser,name='create_user'),
    path('add_attendance/<int:id>',views.add_attendance,name='add_attendance'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('staff_login/<int:id>',views.staff_login,name='staff_login'),
    path('admin_attendance/<int:id>',views.admin_user_attendance,name='admin_attendance'),
    path('update_user/<int:id>',views.update_user,name='update_user'),
    path('update_attendance/<int:id>/<int:value>',views.update_attendance,name='update_attendance'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('delete_attendance/<int:id>/<int:value>',views.delete_attendance,name='delete_attendance'),

]