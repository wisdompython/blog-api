from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


# from .views import PostDetail,PostView,PostList
urlpatterns = [

    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('create-posts/',views.CreatePostView.as_view(), name='create-post'),
    path('post-detail/<str:slug>/',views.PostDetailView.as_view(), name='post-detail')
    # path('post-count/<str:owner_name>/', views.PostCountByOwnerView.as_view(), name='post-count-by-owner'),
    # path('comments/', views.CommentList.as_view()),
    # path('comments23555/<int:pk>/', views.CommentDetail.as_view()),
    # path('categories/', views.CategoryList.as_view()),
    # path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    # path('ratings/', views.RatingList.as_view()),
    # path('ratings/total/<int:post_id>/', PostTotalRating.as_view(), name='post-total-rating'),
    # path('ratings/<int:pk>/', views.RatingDetail.as_view()),
    #path('post-view/', views.PostviewedList.as_view()),
    #path('post-view/<int:pk>/', views.PostviewedDetail.as_view()),
    # path('post-count/', views.PostView.as_view(), name='post-count'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
