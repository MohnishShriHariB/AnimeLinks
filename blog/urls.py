from django.urls import path
from blog import views as v1
from portfolio_1 import views as v2
app_name="blog"
urlpatterns = [
    path('',v1.all_blogs,name='all_blogs'),
    path('<int:blog_id>',v1.detail,name='detail'),
    path('home',v2.home,name='home'),
]
