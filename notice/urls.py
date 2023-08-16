from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('notice/',views.index,name='Notice'),
     path('aboutus/',views.aboutus,name='ABoutus'),
     path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)

