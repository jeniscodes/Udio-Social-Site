
from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("following/<int:profile_id>", views.following, name="following"),
#     path("login", views.login_view, name="login"),
#     path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", views.register, name="register"),
#     path('open_tweet/<int:tweet_id>',views.open_tweet,name="open_tweet"),
#     path('profile/<int:user_id>',views.profile,name="profile"),

#     path('deletetweet/<int:tweet_id>',views.deletetweet,name="deletetweet"),
#     #API Routes
#     path("tweets",views.compose,name="compose"),
#     path("feed/<int:profile_id>",views.feed,name="feed"),
#     path("like/<int:tweet_id>",views.like,name="like"),
#     path("follow/<int:user_id>",views.follow,name="follow"),
#     path("tweetdetails/<int:tweet_id>",views.tweetdetails,name="tweetdetails"),
#     path("editsave/<int:tweet_id>",views.editsave,name="editsave"),

   
#     path("post/<int:tweet_id>",views.comment_post,name="comment_post"),
    
#     path("deletecomment/<int:comment_id>",views.deletecomment,name="deletecomment"),
#     path("comments/<int:tweet_id>",views.comments,name="comments")

# ]

urlpatterns = [
    path('',views.home),
]

