from django.urls import path, include
from watchlist_app.api import views

urlpatterns = [
    path('list/', view=views.WatchListView.as_view(), name='watch_list_view'),
    path('<int:id>/', view=views.WatchListDetailView.as_view(), name='watch_list_detail_view'),
    path('platform/', view=views.StreamingPlatformView.as_view(), name='platform_list_view'),
    path('platform/<int:id>/', view=views.StreamingPlatformDetailView.as_view(), name='platform_detail_view'),
    # path('list/', movie_list, name='movie_list'),
    # path('<int:id>', movie_detail, name='movie_detail'),
]
