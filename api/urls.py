from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # path('', views.products, name='products'),
    # path('<int:id>', views.product, name='product'),
    path("auth/", obtain_auth_token),
    path('', views.ProductApiView.as_view(), name='product'),
    path('<int:pk>/', views.GetProduct.as_view(), name='product'),
    path('posts/', views.PostView.as_view({'get': 'list', 'post': 'create'}), name='posts'),
    path('posts/<int:pk>', views.PostView.as_view({'get': 'retrieve', 'put': 'update'}), name='posts')
    # path('', views.function_api_view, name='product'),
    # path('<int:pk>/', views.function_api_view, name='product')
]
