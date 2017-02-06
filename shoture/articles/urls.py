from django.conf.urls import url
from .views import article_list


urlpatterns = [
    url(r'^articles/$', article_list),
]