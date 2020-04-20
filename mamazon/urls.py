from django.urls import path
from . import views

# アプリ名： 'product-list' のようにbase.htmlで action={% url 'mamazon:product-list' %}
app_name = 'mamazon'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    # pk = primary key
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
]
