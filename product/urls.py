import patterns as patterns
from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ShowView.as_view(), name='show'),
    path('details/<int:id>', views.DetailsView.as_view(), name='details'),
    # path('checkout_cart', views.signin, name='account_login'),
    # path('logout/', views.signout, name='account_logout'),
    # path('signup/', views.signup, name='account_signup'),
    # url(r'^accounts/login$', 'django.contrib.auth.views.login'),
]

