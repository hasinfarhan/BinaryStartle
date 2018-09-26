from django.conf.urls import url
from . import views
from anchor import views as anchor_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_signup$', views.login_signup_page, name='login_signup_page'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^chathistory$', views.chathistory, name='chathistory'),
    url(r'^talk2pok_faq$', views.pokfaq, name='talk2pok_faq'),
    url(r'^talk2pok_profile$', views.pokprofile, name='talk2pok_profile'),
    url(r'^', anchor_views.forbidden_message, name='forbidden_msg'),
]
