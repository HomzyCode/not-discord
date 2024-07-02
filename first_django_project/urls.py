
from django.contrib import admin
from django.urls import path, include

# url routing within the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
