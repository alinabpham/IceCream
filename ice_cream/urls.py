from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ice_cream/home_page.html')),
    url(r'^order/$', views.orderview, name='order_view'),
    url(r'^order/success$', TemplateView.as_view(template_name='ice_cream/success.html')),
    url(r'^view/(?P<option_type>)/$', views.optionview, name='option_view')
]
