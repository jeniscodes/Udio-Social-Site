document.addEventListener('DOMContentLoaded', function() {
  

  
   
    document.querySelector('#temporary').style.display = 'none';
    const tweet_btn=document.querySelector('#tweet_btn');
    const tweet=document.querySelector('#tweet');
    console.log(tweet);
    
    tweet_btn.disabled=true;

    document.querySelector('#tweet').onkeyup= function(){
  
    if (tweet.value.length > 0)
    {
    
        tweet_btn.disabled=false;
    }
    else {
        tweet_btn.disabled=true;
    }


    
}





   
    document.querySelector('#tweet_btn').onclick = function(){
        const content=document.querySelector('#tweet').value;
        document.querySelector('#temporary').style.display = 'block';
        const element = document.createElement('div');
        element.setAttribute("id", "temp");
        element.innerHTML=`<p class="contenttweet"><pre>${content}  </pre>  <hr> </p> `
        

      
        document.querySelector('#tempp').innerHTML= element.innerHTML;
        
        
        console.log(content);
        fetch('/tweets',{
            method:'POST',
            body:JSON.stringify({
                content:`${content}`
                
            })
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result.message);
        });

          


       

        setTimeout(load_feed, 3000) 
        setTimeout(function(){document.querySelector('#temporary').style.display = 'none';},2999);
        document.querySelector('#tweet').value='';
        tweet_btn.disabled=true;
        document.querySelector('#tweet').placeholder='Share your thoughts';


        


        return false;  
       
    }

    document.querySelector('#edit_btn').onclick = function(){
       console.log
    }

   
    
});


function load_feed(){
    const feedelement=document.createElement('div');
    

        
    

        fetch('/feed/0')
        .then(response=>response.json())
        .then(tweets=>{
            tweets.forEach(function(tweets){
                console.log(tweets);
                id=tweets['id'];
                tweeter=tweets['tweeter'];
                contents=tweets['content'];
                timestamp=tweets['timestamp'];
                likes=tweets['likes'];
                comments=tweets['comments'];
                tweeterid=tweets['tweeterid'];
                tweeterusername=tweets['tweeterusername'];
                image=tweets['image'];
                liked=tweets['liked'];
                if ( liked==='yes'){
                    love='<i class="fa fa-heart" style="color:crimson"></i>'
                }
                else{
                    love='<i style="font-size:14px" class="fa">&#xf08a;</i> '
                }
                const element = document.createElement('div');
                element.innerHTML=`<div class="card" style="width: 45rem;">
                <ul class="list-group list-group-flush">

                <li class="list-group-item tweetcard"> <div  onclick="location.href='/open_tweet/${id}'">
      <img class="rounded-circle z-depth-2" alt="100x100" data-holder-rendered="true" src='/media/images/${image}'>  
      <span class="link"> &nbsp; ${tweeter} </span> <span class="userid"> <a href= profile/${tweeterid} class="userid"> @${tweeterusername} </a> ${timestamp} </span>
      <p class="contenttweet"><pre>${contents}  </pre>  <hr> </p>  </div> 
      <div class="block"> 
         <div onclick="like(this)" id="like${id}" class="subblock" data-id="${id }"> 
          ${love}
          

          ${likes }  
        
        
        
          &nbsp;
        </div> <div  class="subblock" onclick="location.href='/open_tweet/${id}'" > 
          <i class="fa fa-comment-o" aria-hidden="true"></i>  ${comments } 
        
     
      </div>  
    </div> 
    </li>
                
                   `
                feedelement.append(element);
    
            })
            document.querySelector('#feed').innerHTML= feedelement.innerHTML

            
    
        }); 
        


}





function like(tweet){
    element=document.getElementById(`like${tweet.dataset.id}`)
    console.log(tweet.dataset.id);
    fetch(`/like/${tweet.dataset.id}`)
    .then(response=>response.json())
    .then(result=>{
        console.log(result.message);
        if (result.like_create==="yes"){
        element.innerHTML=` <i class="fa fa-heart" style="color:crimson"></i> ${result.likes} `
        }
        else{
            element.innerHTML=`<i style="font-size:14px" class="fa">&#xf08a;</i>  ${result.likes}`
        }
    });
}


    
   
    
    

    





        
