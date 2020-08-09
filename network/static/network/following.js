document.addEventListener('DOMContentLoaded', function() {
    

    const user_id=document.querySelector('#feed').getAttribute('data-id');
  
   

   
    
   
    document.querySelector('#compose').onsubmit = function(){
        const content=document.querySelector('#tweet').value;
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

        return false;  
       load_feed();
    }

    document.querySelector('#edit_btn').onclick = function(){
       console.log
    }

   
    
});




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


    
    
   
    
    

    





        
