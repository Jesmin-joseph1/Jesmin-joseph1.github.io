from django.urls import path
from shopapp import views

urlpatterns = [
    path('', views.Index, name='shoppage'),
    path('about', views.About, name='aboutpage'),
    path('contact', views.Contact, name='contactpage'),
    path('news', views.News,name = 'newspage'),
    path('cat', views.CategoryPage,name = 'catpage'),
    path('product/<str:cname>/',views.ProductView,name='productviewpage'),
    path('detail/<str:pname>/', views.Productdetail, name='productdetailpage'),
    path('search', views.search, name='searchpage'),
]
