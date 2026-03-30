from django.urls import path
from polls import views

urlpatterns = [
	path('abc', views.index, name='index'),
	path('html', views.testHtml),
	path('visu', views.visu),
]
