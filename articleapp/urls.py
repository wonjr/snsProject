from django.urls import path
from articleapp import views
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView


app_name = "articleapp"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('<int:pk>/like', views.like, name='like'),
    path('<int:pk>/dislike', views.dislike, name='dislike'),
]
