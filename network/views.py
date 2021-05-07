import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import requests
now = datetime.now()

from .models import User, Tweet, Comment, Like, Follow




# Create your views here.
# api_key= '16000001c1b6ba6e216778b178995cd094afc373'
# trafficapi_url = 'https://bin.mapletrack.com/aaa.php?page=Stats&ts_id=21&date=12&group1=287&group2=288&group3=1&date_s=2021-05-06&date_e=2021-05-06&timezone=-5:00&api_key=16000001c1b6ba6e216778b178995cd094afc373'

# plugrush='https://admin.plugrush.com/api/v2/campaigns?email=dinoevolution%40gmail.com&hash=5cb82c7cf82d2a12a33c117fcba9178d65f9ca13ab9726ccaa49f634f074d684&timestamp=1620360612'

def revenue_data():
    res = requests.get('https://bin.mapletrack.com/aaa.php?page=Stats&ts_id=21&date=12&group1=287&group2=282&group3=1&date_s=2021-05-06&date_e=2021-05-06&timezone=-5:00&api_key=16000001c1b6ba6e216778b178995cd094afc373')
    response = res.content.decode('utf8').replace("","")
    data = json.loads(response)
    s = json.dumps(data, indent=4,sort_keys=True)
    return data

# def plugrushapi():
#     res = requests.get('https://admin.plugrush.com/api/v2/stats/advertiser/websites?email=dinoevolution%40gmail.com&hash=b50f4dc32eabed086149dde5b9c8722f65005487aff7be234756f5406d4e030c&timestamp=1620372608&campaigns=%7840119&limit=0&offset=0&fbclid=IwAR1_VVkz7qetiWGq_TjR_6j2Uu29MPQjMbNjgQ1HW4P51dg9lEOYD09m7jQ')
#     response = res.content.decode('utf8').replace("","")
#     data = json.loads(response)
#     print(data)
#     s = json.dumps(data, indent=4,sort_keys=True)
#     return data    

def home(request):   
    data_traffic =revenue_data()
    # data_plugrush = plugrushapi()

    # revenue = []
    # r = len(data.revenue)
    # print(r)
    # for i in range(0,r):
    #     a = data.revenue
    #     revenue.append(a)
    # cost = data.cost
    # print(revenue)
    context={
        'data_traffic': data_traffic
    }
    return render(request, 'network/home.html',context)










# @login_required
# def index(request):
    
#     #get all tweets in the database

#     tweets=Tweet.objects.all()

#        #order them by timestamp in descending order
#     tweets=tweets.order_by("-timestamp").all()
#     tweets_list=[]
    
#     for tweet in tweets:
#         #get the likes in the individual  tweet
#         likes=tweet.likes.all()
#         #whether the tweet is liked by the login user or not
#         liked=tweet.likes.filter(liker=request.user)
#         #get all the comments in the tweet
#         comments=tweet.comments.all()
#         #get the number of comments and likes in the tweet
#         number_likes=len(likes)
#         number_comments=len(comments)
#         #all details for an individual tweet
#         tweet_details={
#             "id": tweet.id,
#             "tweeter":tweet.owner.name,
#             "tweeterid":tweet.owner.id,
#             "tweeterusername":tweet.owner.username,
#             "content":tweet.content,
#             "timestamp":tweet.timestamp.strftime(" %I:%M %p %d %b, %Y"),
#             "likes":number_likes,
#             "comments":number_comments,
#             "image":tweet.owner.imagefile,
#             "liked":liked
            
#         }
#         #apeend the tweets details in a list
#         tweets_list.append(tweet_details)

#         #divide the list into pages with 10 tweets per page

#     paginator = Paginator(tweets_list, 10) # Show 10 tweets per page.
    

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
 

     
#       #render the index page with tweet details   
#     return render(request, "network/index.html",{'page_obj': page_obj})



# @login_required
# def profile(request,user_id):
#     #get the profile of the user requested
#     user=User.objects.get(pk=user_id)
#     #get the followers and following list of the user
#     followers=user.followedbylist.all()
#     followings=user.followinglist.all()
#     #check whether the logged in user has followed the profile or not
#     followed=Follow.objects.filter(following=user,follower=request.user)
#     number_followers=len(followers)
#     number_followings=len(followings)
#     #filter the tweets by the user
#     tweets=Tweet.objects.filter(owner=user)

       
#     tweets=tweets.order_by("-timestamp").all()

#     tweets_list=[]
    
    
#     for tweet in tweets:
        
#         likes=tweet.likes.all()
#         liked=tweet.likes.filter(liker=request.user)
#         comments=tweet.comments.all()
#         number_likes=len(likes)
#         number_comments=len(comments)
#         tweet_details={
#             "id": tweet.id,
#             "tweeter":tweet.owner.name,
#             "tweeterid":tweet.owner.id,
#             "tweeterusername":tweet.owner.username,
#             "content":tweet.content,
#             "timestamp":tweet.timestamp.strftime(" %I:%M %p %d %b, %Y"),
#             "likes":number_likes,
#             "comments":number_comments,
#             "image":tweet.owner.imagefile,
#             "liked":liked
            
#         }
#         tweets_list.append(tweet_details)

#     paginator = Paginator(tweets_list, 10) # Show 10 contacts per page.
 

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
  
 
   
    


# #send details of number of followers , followings, tweets and followed by the logged in user or not
#     return render(request,"network/profile.html",{'user':user,'following':following,'followers':followers,"followed":followed,
#     "followers":f'{number_followers}',"followings":f'{number_followings}','page_obj': page_obj})



# @login_required
# def following(request, profile_id):
#     #get the following feed
#     user=User.objects.get(pk=profile_id)
#     #get the following list of the user
#     following=user.followinglist.all()
#     # add the user and followers in a list
    
#     following=[person.following.id for person in following]
#     following.append(profile_id)
#     #get the list of tweets made by followers and the user
#     tweets=(Tweet.objects.filter(owner__in=following))
#     tweets=tweets.order_by("-timestamp").all()
#     tweets_list=[]
#     for tweet in tweets:
#         likes=tweet.likes.all()
#         liked=tweet.likes.filter(liker=request.user)
#         comments=tweet.comments.all()
#         number_likes=len(likes)
#         number_comments=len(comments)

#         tweet_details={
#             "id": tweet.id,
#             "tweeter":tweet.owner.name,
#             "tweeterid":tweet.owner.id,
#             "tweeterusername":tweet.owner.username,
#             "content":tweet.content,
#             "timestamp":tweet.timestamp.strftime(" %I:%M %p %d %b, %Y"),
#             "likes":number_likes,
#             "comments":number_comments,
#             "image":tweet.owner.imagefile,
#             "liked":liked
            
#         }
#         tweets_list.append(tweet_details)
#     paginator = Paginator(tweets_list, 10) # Show 10 contacts per page.
 

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
 

     
         
    

    

     
         
#     return render(request, "network/following.html",{'page_obj': page_obj})
    
        


         
# @login_required
# @csrf_exempt
# def compose(request):
#     #function to compose a tweet
#     if request.method!="POST":
#         return JsonResponse({"error": "POST request required."}, status=400)

#     data = json.loads(request.body)
#     content=data.get("content","")
#     #create the tweet
#     tweet=Tweet(
#     owner=request.user,
#     content=content
#     )
#     tweet.save()

#     return JsonResponse({"message":"Tweet sucessfully created."}, status=201)

# @csrf_exempt
# def editsave(request,tweet_id):
#     if request.method!="POST":
#         return JsonResponse({"error": "POST request required."}, status=400)

#     data = json.loads(request.body)
#     content=data.get("content","")
#     tweet=Tweet.objects.get(pk=tweet_id)
#     tweet.content=content
    
#     tweet.save()

#     return JsonResponse({"message":"Tweet sucessfully edited."}, status=201)


# #api to load the feed
# def feed(request,profile_id):
#     #loading feed for all posts
    

#     tweets=Tweet.objects.all()
        
        
        
    

#     tweets=tweets.order_by("-timestamp").all()
#     tweets_list=[]
#     paginator = Paginator(tweets_list, 10) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     #loading only 10 tweets for the page if there are more than 10 tweets
#     if len(tweets)>10:
#         for i in range(10):
            

#             likes=tweets[i].likes.all()
#             #whether the user has liked the tweet or not
#             try:
#                 liked=tweets[i].likes.get(liker=request.user)
#                 liked="yes"
#             except:
#                 liked="no"
            
            
#             comments=tweets[i].comments.all()
#             number_likes=len(likes)
#             number_comments=len(comments)
#             image=os.path.basename(os.path.normpath(tweets[i].owner.imagefile.path))
#             tweet_details={
#             "id": tweets[i].id,
#             "tweeter":tweets[i].owner.name,
#             "content":tweets[i].content,
#             "timestamp":tweets[i].timestamp.strftime(" %I:%M %p %d %b, %Y"),
#             "likes":number_likes,
#             "comments":number_comments,
            
#             "tweeterid":tweets[i].owner.id,
#             "tweeterusername":tweets[i].owner.username,
            
#             "image":image,
#             "liked":liked
#         }
#             tweets_list.append(tweet_details)
#     else:
        

# #if there are less than 10 tweets
 
#         for tweet in tweets:

            
#             likes=tweet.likes.all()
#             try:
#                 liked=tweet.likes.get(liker=request.user)
#                 liked="yes"
#             except:
#                 liked="no"
#             print(liked)
            
#             comments=tweet.comments.all()
#             number_likes=len(likes)
#             number_comments=len(comments)
#             image=os.path.basename(os.path.normpath(tweet.owner.imagefile.path))
#             tweet_details={
#             "id": tweet.id,
#             "tweeter":tweet.owner.name,
#             "content":tweet.content,
#             "timestamp":tweet.timestamp.strftime(" %I:%M %p %d %b, %Y"),
#             "likes":number_likes,
#             "comments":number_comments,
            
#             "tweeterid":tweet.owner.id,
#             "tweeterusername":tweet.owner.username,
            
#             "image":image,
#             "liked":liked
#         }
#             tweets_list.append(tweet_details)
        
 
    
    
#     return JsonResponse(tweets_list,safe=False)







# @login_required
# #function to like or unlike a tweet
# def like(request, tweet_id):
# #get the tweet which is liked or unliked
#     tweet=Tweet.objects.get(pk=tweet_id)
#     print(tweet_id)
#     #check whether the tweet is like by loginuser
#     check=Like.objects.filter(likedtweet=tweet,liker=request.user)
#     likes_list=[]
#     #if user is liking the tweet
#     if len(check)<1:
#         liketweet=Like(
#         liker=request.user,
#         likedtweet=tweet)
#         liketweet.save()
#         likes=tweet.likes.all()
#         comments=tweet.comments.all()
#         number_likes=len(likes)
#         number_comments=len(comments)
#         #list of all user who has liked the tweet
#         for like in likes:
    
#             like_details={
#                 "id": like.id,
#                 "liker":like.liker.username,
#                 "image":os.path.basename(os.path.normpath(like.liker.imagefile.path))
                
#             }
#             likes_list.append(like_details)


#         #send the updated likes list and liked numbers 
#         return JsonResponse({"message":"Tweet sucessfully liked.", "likes":f'{number_likes}',
#         "comments":f'{number_comments}',"l_likes" :likes_list,"like_create":"yes"},
#         status=201)
        
#     else:
#         # if user is unliking the tweet delete the liked object
#         check.delete()
#         likes=tweet.likes.all()
#         comments=tweet.comments.all()
#         number_likes=len(likes)
#         number_comments=len(comments)
#         for like in likes:
    
#             like_details={
#                "id": like.id,
#                 "liker":like.liker.username,
#                 "image":os.path.basename(os.path.normpath(like.liker.imagefile.path))
                
#             }
#             likes_list.append(like_details)

#             #send the updated likes list and liked numbers 
        
#         return JsonResponse({"message":"Tweet sucessfully disliked.","likes":f'{number_likes}',
#         "comments":f'{number_comments}',"l_likes" :likes_list,"like_create":"no"}, status=201)

# @login_required
# def follow(request, user_id):

#     #get the profilw of user

#     profile=User.objects.get(pk=user_id)
#    #check whether the user has been followed or not
#     check=Follow.objects.filter(following=profile,follower=request.user)
#     print(check)

#     if len(check)<1:
#         #follow the user
#         followprofile=Follow(
#         follower=request.user,
#         following=profile)
#         followprofile.save()
#         followers=profile.followedbylist.all()
#         followings=profile.followinglist.all()
#         #update the number of followings and unfollowers
#         number_followers=len(followers)
#         number_followings=len(followings)
#         followed='yes'

        
#         return JsonResponse({"message":"profile sucessfully followed.", "followers":f'{number_followers}',"followings":f'{number_followings}', 
#         "followed":followed},status=201)
        
#     else:
#         #unfollow the user
#         check.delete()
#         followers=profile.followedbylist.all()
#         followings=profile.followinglist.all()
#         #update the number of followings and unfollowers
#         number_followers=len(followers)
#         number_followings=len(followings)
#         followed='no'

        
#         return JsonResponse({"message":"profile sucessfully unfollowed.", "followers":f'{number_followers}',"followed":followed,"followings":f'{number_followings}'}, status=201)



# @login_required
# @csrf_exempt
# def comment_post(request,tweet_id):
#     #comment to a tweet
 

#     data = json.loads(request.body)
#     tweet=Tweet.objects.get(pk=tweet_id)
    
#     content=data.get("content","")
#     #create the comment object

#     comment=Comment(
#     commenter=request.user,
#     comment=content,
#     commentedtweet=tweet

#     )
#     comment.save()
#     #updated number of comments and likes
#     likes=tweet.likes.all()
#     comments=tweet.comments.all()
#     number_likes=len(likes)
#     number_comments=len(comments)

#      #send the updated number of comments and likes
#     return JsonResponse({"message":"Comment sucessfully created.","likes":f'{number_likes}',"comments":f'{number_comments}'}, status=201)

# @login_required
# #function to open tweet
# def open_tweet(request,tweet_id):
#     #get tge tweet the likes, comments on it
#     tweet=Tweet.objects.get(pk=tweet_id)
#     likes=tweet.likes.all()
#     comments=tweet.comments.all()
#     comments=comments.order_by("-pk").all()
#     number_likes=len(likes)
#     number_comments=len(comments)
#     #whether the tweet is liked by logged in user or not
#     liked=tweet.likes.filter(liker=request.user)


#     return render(request, "network/tweet.html",{'tweet':tweet,'likes':likes,'comments':comments,'num_likes':
#     number_likes,'num_comments':number_comments,'liked':liked})


# @login_required
# def comments(request,tweet_id):
#     #api to get list of comments
#     tweet=Tweet.objects.get(pk=tweet_id)
#     #get comments in the tweet
#     comments=tweet.comments.all()
#     comments=comments.order_by("-pk").all()
#     comment_list=[]
#     for comment in comments:
#         image=os.path.basename(os.path.normpath(comment.commenter.imagefile.path))
#         comment_details={
#             "id": comment.id,
#             "commenter":comment.commenter.name,
#             "commenterusername":comment.commenter.username,
#             "content":comment.comment,
#             "image":image,
#             "commenterid":comment.commenter.id

#         }
#         comment_list.append(comment_details)

#         #send the comment details 

#     return JsonResponse(comment_list,safe=False)



# @login_required
# def tweetdetails(request,tweet_id):

#     #fetch the particular tweet
#     tweet=Tweet.objects.get(pk=tweet_id)
#     content=tweet.content

#     return JsonResponse({"content":content}, status=201)




# @login_required
# def deletetweet(request,tweet_id):
#     #get the tweet to be deleted
#     tweet=Tweet.objects.get(pk=tweet_id)
#     tweet.delete()
#     return JsonResponse({"message":"tweet sucessfully deleted."}, status=201)


# @login_required
# def deletecomment(request,comment_id):
#     #get the comment to be deleted
#     comment=Comment.objects.get(pk=comment_id)
    
#     comment.delete()
#     tweet=comment.commentedtweet
#     comments=tweet.comments.all()
#     ncomments=len(comments)
#     print(ncomments)
#     return JsonResponse({"message":"comment sucessfully deleted.","comments":ncomments}, status=201)

# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "network/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "network/login.html")


# @login_required
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("login"))


# def register(request):
#     if  request.method=="POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         name=request.POST["name"]
#         try:
            
        
#             imagefile =request.FILES["imagefile"]

#         except:
#             user=User.objects.get(username='anon')

#             imagefile=user.imagefile
        
    
        
        

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
    
#         if password != confirmation:
#             return render(request, "network/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password, imagefile=imagefile, name=name)
#             user.save()
#         except IntegrityError:
#             return render(request, "network/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "network/register.html")



