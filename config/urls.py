from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Вынесла users
    path('api/', include('habits.urls')),
]
