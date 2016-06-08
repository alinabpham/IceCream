from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ice_cream/home_page.html')),
    url(r'^order/$', views.orderview, name='order_view'),
    url(r'^order/success/$', TemplateView.as_view(template_name='ice_cream/success.html')),
    url(r'^options/(?P<option_type>\w+)/?$', views.optionview, name='option_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)