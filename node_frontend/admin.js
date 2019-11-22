function notify_all(){
    var message = document.getElementsByName("message")[0].value;
    $.ajax({

      url : 'http://192.168.2.158:8001/getdata/',
      type : 'POST',
      data : JSON.stringify({"message":message}),
      success : function(data) {              
        //  console.log(data);
         
      },
      
      });
}
const check = () => {
    if (!('serviceWorker' in navigator)) {
      throw new Error('No Service Worker support!')
    }
    if (!('PushManager' in window)) {
      throw new Error('No Push API Support!')
    }
    
    
  }
  const registerServiceWorker = async () => {
    const swRegistration = await navigator.serviceWorker.register("service.js")
    return swRegistration
  }
  const requestNotificationPermission = async () => {
    const permission = await window.Notification.requestPermission()
    // value of permission can be 'granted', 'default', 'denied'
    // granted: user has accepted the request
    // default: user has dismissed the notification permission popup by clicking on x
    // denied: user has denied the request.
    if (permission !== 'granted') {
      throw new Error('Permission not granted for Notification')
    }
    else{
      console.log("cc");
    }
  }
  const main = async () => {
    check()
    const swRegistration = await registerServiceWorker()
    const permission = await requestNotificationPermission()
    
  }
  main(); //we will not call main in the beginning.



  function upload() {
    // event.preventDefault();
    var data = new FormData($('form').get(0));
    
    $.ajax({
        url: 'http://localhost:8000/postdata',
        type: 'POST',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            alert('success');
        }
    });
    return false;
    }
    
  