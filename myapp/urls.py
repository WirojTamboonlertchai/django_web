from django.urls import path, re_path

from . import views



app_name = 'myapp'
urlpatterns = [
	# path('', views.index, name="index"),
	# path('add/<int:num_a>/<int:num_b>/', views.add, name="add"),
	# path('overview', views.overview, name="overview"),
	# path('product/<int:id>', views.overview, name="product"),
	# path('about/contact/', views.contact, name="contact"),
	# path('social', views.social, name="social"),

	path('news/<str:p>', views.news, name="news_page"),
	path('news/', views.news, name="news"),
	# path(),
]