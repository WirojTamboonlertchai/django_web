from django.urls import path
from . import views

# คือการสร้าง url config
app_name = 'polls' #namespace
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'), # ต้องระบุชื่อให้ template เหตุผลส่วนหนึ่งคือเอาไว้ใช้กับ tag 'url'
	path('<int:question_id>/results', views.results, name='results'),
	path('<int:question_id>/vote', views.vote, name='vote'),
	path('create/', views.create, name="create"),
	path('<int:question_id>/delete/', views.delete, name="delete"),
	path('<int:question_id>/edit/', views.edit, name="edit"),
	path('login/', views.login, name="login"),
	# path('logout/', views.logout, name="logout"),
	# path('fav', views.fav, name="fav"),
	# path('item01', views.item01, name="item01"),
	# path('item05', views.item05, name="item05"),
]