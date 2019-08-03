from django.urls import path
from . import views
#正在部署的应用名称
app_name = 'article'

urlpatterns = [
    path("article_list/",views.article_list,name = 'article_list',),
    path('article-detail/<int:id>/',views.article_detail,name = 'article_detail'),






]
