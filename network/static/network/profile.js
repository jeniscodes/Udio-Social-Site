document.addEventListener('DOMContentLoaded', function() {

    const profile_id=document.querySelector('#follow').getAttribute('data-id')
  
    document.getElementById('follow').addEventListener('click', ()=>follow(profile_id));
    

   
    

   
    
});


function follow(user){
    element=document.getElementById('follownum')
    fetch(`/follow/${user}`)
    .then(response=>response.json())
    .then(result=>{
        console.log(result.message);
        if ( result.followed === 'yes'){
            f="Following"

        }
        else
        {
            f="Follow"
        }
        
    
        element.innerHTML=`<strong style="color: black;"> ${result.followings} </strong> Followings
        <strong style="color: black;"> ${result.followers} </strong>  Followers`
        document.getElementById('follow').innerHTML=`${f}`

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



    
    
    
   
    
    

    





        
