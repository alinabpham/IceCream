from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^order/$', views.orderview, name='order_view'),
    url(r'^order/success$', TemplateView.as_view(template_name='ice_cream/success.html')),
    url(r'^view/(?P<option_type>)/$', views.optionview, name='option_view')
]
