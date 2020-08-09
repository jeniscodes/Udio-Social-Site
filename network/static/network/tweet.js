document.addEventListener('DOMContentLoaded', function() {
 
    document.querySelector('#editcontent').style.display = 'none';
    document.querySelector('#temporary').style.display = 'none';

  
    


    window.user=document.querySelector('#user').getAttribute('data-user');
   
    window.owner=document.querySelector('#user').getAttribute('data-owner');
    
    window.tweet_id=document.querySelector('#deleteit').getAttribute('data-id');


    window.tweet_btn=document.querySelector('#comment_submit');
    window.tweet=document.querySelector('#commentedtext');
    console.log(tweet);
    tweet_btn.disabled=true;

    tweet.onkeyup= function(){
  
    if (tweet.value.length > 0)
    {
    
        tweet_btn.disabled=false;
    }
    else {
        tweet_btn.disabled=true;
    }
}
 
    
});


function load_comment(){
    const commentelement=document.createElement('div');
    fetch(`/comments/${tweet_id}`)
    .then(response=>response.json())
    .then(comments=>{
        comments.forEach(function(comments){
            console.log(comments['id']);
            id=comments['id'];
            commenter=comments['commenter'];
            comment=comments['content'];
            image=comments['image'];
            username=comments['commenterusername'];
            commenterid=comments['commenterid']
            const element = document.createElement('div');
            if ( user == username || owner == user )
            {
               
                del=`<span id="deletecmt"> 
                <i class="fa fa-trash" data-toggle="modal" data-target="#exampleModal2" aria-hidden="true" data-id=${id} onclick="deletethis(this)"></i>
                 </span>`
            }
            else{
              
                del=''
            }
            element.innerHTML=`<li class="list-group-item commentcard border-bottom-0" id=comment${id}> 
        <img class="rounded-circle z-depth-2" alt="100x100" data-holder-rendered="true" src='/media/images/${image}'>  
        <span class="link"> &nbsp; ${commenter} </span> <a href= '/profile/${commenterid}' class="userid">  @${username} </a>
        ${del}
        <p class="contenttweet"> <pre>${comment} </pre>  </p> 
        </li>`
            commentelement.append(element);

        })
        console.log(document.querySelector('#commentsbox'));
        document.querySelector('#commentsbox').innerHTML= commentelement.innerHTML
    });


}

function like(tweet){
    const likelist= document.createElement('div');
    element=document.getElementById(`like${tweet.dataset.id}`)
    console.log(tweet.dataset.id);
    fetch(`/like/${tweet.dataset.id}`)
    .then(response=>response.json())
    .then(result=>{
        console.log(result.message);
        if (result.like_create==="yes"){
        element.innerHTML=` <i class="fa fa-heart" style="color:crimson"></i>`   
    
        }
        else{
            element.innerHTML=` <i style="font-size:14px" class="fa">&#xf08a;</i>`
            
        }

        document.getElementById('num_likes').innerHTML=`${result.likes}`;
        document.querySelector('#modalbody').innerHTML=''
        result.l_likes.forEach(function(like){
            
            id=like['id']
            liker=like['liker']
            image=like['image']
            const element = document.createElement('div');
            element.innerHTML=`
            <li class="list-group-item tweetcard" >  <img class="rounded-circle z-depth-2" alt="100x100" data-holder-rendered="true" src='/media/images/${image}'>  
         
            <strong> &nbsp; ${liker} </strong> </li>
            `
            likelist.append(element);


        });

        document.querySelector('#modalbody').innerHTML=likelist.innerHTML
        
          
    });
}




function post_comment(tweet){
    const ncomments=document.getElementById('ncomments');
    
     
    const content=document.querySelector('#commentedtext').value;
    document.querySelector('#temporary').style.display = 'block';
    const element = document.createElement('div');
    element.setAttribute("id", "temp");
    element.innerHTML=` <p class="contenttweet"> <pre>${content}</pre>  </p>`
    

  
    document.querySelector('#tempp').innerHTML= element.innerHTML;
    
        console.log(content);
        fetch(`/post/${tweet.dataset.id}`,{
            method:'POST',
            body:JSON.stringify({
                content:`${content}`
            })
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result.message);
            ncomments.innerHTML=` <i class="fa fa-comment-o" aria-hidden="true" ></i> ${result.comments}`
        });

        document.querySelector('#commentedtext').value='';
        document.querySelector('#comment_submit').disabled=true;
        setTimeout(load_comment,3000);
        setTimeout(function(){document.querySelector('#temporary').style.display = 'none';},3000);


    return false;

    
    }

    function edit(tweet){
        console.log(document.querySelector('#tweetcardbox'));
        document.querySelector('#tweetcardbox').style.display = 'none';
        document.querySelector('#editcontent').style.display = 'block';
        
        fetch(`/tweetdetails/${tweet.dataset.id}`)
    .then(response=>response.json())
    .then(result=>{
        console.log(result.content);
        document.querySelector('#tweetedit').value=result.content;
        

    });
}

    function edit_save (tweet){
        const content=document.querySelector('#tweetedit').value;
        console.log(tweet.dataset.id);
        
        fetch(`/editsave/${tweet.dataset.id}`,{
            method:'POST',
            body:JSON.stringify({
                content:`${content}`,
                
            })
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result.message);
        });

        setTimeout(() => {location.reload()
            
        }, 2000);
        return false;  
      
    }

  

    function deletethis(comment){
        window.id=comment.dataset.id;
    }
    

    function deletecomment (){
        const ncomments=document.getElementById('ncomments');
        commentcard=document.getElementById(`comment${id}`);
        commentcard.style.animationPlayState = 'running';

      
        fetch(`/deletecomment/${id}`)
        .then(response=>response.json())
        .then(result=>{
            console.log(ncomments);
            //console.log(result.message);
            ncomments.innerHTML=` <i class="fa fa-comment-o" aria-hidden="true" ></i> ${result.comments}`;
        });
        console.log(ncomments);
        
        
        setTimeout(load_comment,3000);
        
      

        return false;  
    }


    function deletetweet (tweet){
        
        
        fetch(`/deletetweet/${tweet.dataset.id}`)
        .then(response=>response.json())
        .then(result= setTimeout(function()
        {
            console.log(result.message);
        },3000)
        );

        
        setTimeout(function(){
            location.href='/';
        },3000);

        return false;



    }

   

   
   
    

    


    
    
   
    
    

    





        
