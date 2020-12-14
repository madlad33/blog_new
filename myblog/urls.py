from . import views
from django.urls import path, include
import myblog
from .views import Homeview, BlogDetail,Addview

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('article/<int:pk>', BlogDetail.as_view(), name='article_detail'),
    path('addpost/',Addview.as_view(),name='add_post')
]
