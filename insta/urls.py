from django.urls import path
from insta.views import PostListView


urlpatterns = [
    #local http://127.0.0.1:8000/
    path('',PostListView.as_view(), name='post_list'),

]
