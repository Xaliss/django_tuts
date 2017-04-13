from django.conf.urls import  url
from django.conf.urls.static import static
from . import views



urlpatterns = [
	url(r'^$'         			,views.IndexView.as_view(),       	name='index'),
	url(r'^(?P<pk>[0-9]+)/$'	,views.DetailView.as_view(), 		name='detail'),
	url(r'^sliderz$'  			,views.sliderz,     				name='sliderz'),
	url(r'^levures$'  			,views.levures,     				name='levures'),
	url(r'^route$'    			,views.route,       				name='route'),
	 

]


