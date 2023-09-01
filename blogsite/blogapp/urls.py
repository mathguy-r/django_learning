from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.BlogpageView.as_view(), name='blogpage'),
    path('article/<int:pk>', views.BlogContentView.as_view(), name='blog-read'),
    path('create_blog/', views.CreateBlogView.as_view(), name='blog-create'),
    path('article/<int:pk>/update/', views.UpdateBlogView.as_view(), name='blog-update'),
    path('article/<int:pk>/delete/', views.DeleteBlogView.as_view(), name='blog-delete'),
]
