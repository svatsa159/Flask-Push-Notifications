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
  // importScripts('localforage.min.js');
  
  
  
  
  function process() {
    var user;
    // var user = document.getElementsByName("u")[0].value
    localforage.getItem('user').then(function (value) {
        // Do other things once the value has been saved.
        console.log(value);
        user = value;
        data = JSON.stringify({"logged_in":user})
        $.ajax({

          url : 'http://192.168.2.158:8001/process/',
          type : 'POST',
          data : data,
          success : function(data) {              
             console.log(data);
             
          },
          
          });
    }).catch(function(err) {
        // This code runs if there were any errors
        // console.log(err);
        
    });
    
    // console.log(data);
    
    
    }
    
  