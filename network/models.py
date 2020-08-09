from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name=models.TextField(null=True)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

class Tweet(models.Model):
    owner=models.ForeignKey("User",on_delete=models.CASCADE,related_name="tweeter")
    
    content=models.TextField(blank=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return{
            "id": self.id,
            "tweeter":self.owner.email,
            "content":self.content,
            "timestamp":self.timestamp.strftime("%d %b, %Y - %I:%M %p")
        }

class Comment(models.Model):
    commenter=models.ForeignKey("User",on_delete=models.CASCADE,related_name="listcomments")
    comment=models.TextField(blank=False)
    commentedtweet=models.ForeignKey("Tweet",on_delete=models.CASCADE,related_name="comments")

class Like(models.Model):
    liker=models.ForeignKey("User",on_delete=models.CASCADE,related_name="listlikes")
    likedtweet=models.ForeignKey("Tweet",on_delete=models.CASCADE,related_name="likes")

class Follow(models.Model):
    follower=models.ForeignKey("User",on_delete=models.CASCADE,related_name="followinglist")
    following=models.ForeignKey("User",on_delete=models.CASCADE,related_name="followedbylist")






