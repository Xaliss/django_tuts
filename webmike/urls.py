from django.conf.urls import url
#from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$'         			,views.IndexView.as_view(),  name='index'),
	# url(r'^(?P<pk>[0-9]+)/$'	,views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/$'	,views.IxeView.as_view(),    name='ixe'),
	url(r'^homezz$'				,views.kilikili,  			 name='kilikili'),
	url(r'^home$' 				,views.home,  				 name='home'),
	url(r'^kala$' 				,views.kalakala,  			 name='kalakala'),
	url(r'^route$' 				,views.route,  				 name='route'),
	url(r'^create$' 			,views.create,  			 name='create'),
	url(r'^update/(?P<id>\d+)$' ,views.update,  			 name='update'),
	url(r'^edit/(?P<id>\d+)$' 	,views.edit,  			 	 name='edit'),
	url(r'^efface/(?P<id>\d+)$' ,views.efface,  			 name='efface'),
]

