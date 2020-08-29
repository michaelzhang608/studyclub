document.addEventListener("DOMContentLoaded", () => {
  console.log("Javascript Loaded")

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // Connect to socketio
  socket.on("connect", () => {

  })

  // Fade out all divs and fade in specific div
  function change_to(div) {
    let all_children = document.querySelector("#main").children
    for (let i = 0; i < all_children.length; i++) {
      $(all_children[i]).fadeOut()
    }

    setTimeout(() => {
      $(div).fadeIn()
    }, 400)
    return false
  }
  
  // TODO

})
