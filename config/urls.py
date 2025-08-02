from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from base.views import home, login, register
from taskmanage.views import task_display, task_create, toggle_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('tasks/', task_display, name='tasks_display'),
    path('add_task/', task_create, name='tasks'),
    path('toggle_complete/<int:task_id>/', toggle_complete, name='toggle_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)