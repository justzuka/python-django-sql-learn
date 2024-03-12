from django.urls import path, include
from MyUserAuth import urls as myuserauth_urls
from workouts import urls as workouts_urls
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # Include Django Admin URLs
    path("myuserauth/", include(myuserauth_urls)),  # Include MyUserAuth app's urlpatterns
    path("workouts/", include(workouts_urls)),  # Include workouts app's urlpatterns
]