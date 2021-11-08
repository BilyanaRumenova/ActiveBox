from django.urls import path

from test_Django.test_app.views import index_page

urlpatterns = (
    path('', index_page, name='index'),
)