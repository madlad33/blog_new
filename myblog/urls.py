from . import views
from django.urls import path, include
import myblog
from .views import Homeview, BlogDetail,Addview,UpdateBlogView,DeleteBlogView,CreateCategoryView,CategoryUrlView

urlpatterns = [
     path('', Homeview.as_view(), name='home'),
    path('article/<int:pk>', BlogDetail.as_view(), name='article_detail'),
    path('addpost/',Addview.as_view(),name='add_post'),
    path('article/<int:pk>/updatepost/',UpdateBlogView.as_view(),name='update_post'),
    path('article/<int:pk>/deletepost/',DeleteBlogView.as_view(),name='delete_post'),
    path('addcategory/', CreateCategoryView.as_view(), name='add_category'),
    path('category/<str:category>/',CategoryUrlView,name='url_category'),
]
