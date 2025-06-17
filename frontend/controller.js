$(document).ready(function () {
  eel.expose(DisplayMessage)
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate('start');
  }

  eel.expose(ShowHome)
  function ShowHome() {
    $('#Oval').attr("hidden", false);
    $('#SiriWave').attr("hidden", true);
  }

  eel.expose(sendText)
  function sendText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `
        <div class="row justify-content-end mb-4">
          <div class="width-size">
          <div class="sender_message">${message}</div>
        </div>
      `;

      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }

  eel.expose(receiveText)
  function receiveText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `
        <div class="row justify-content-start mb-4">
          <div class="width-size">
          <div class="receiver_message">${message}</div>
        </div>
      `;

      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }

  eel.expose(hideLoader)
  function hideLoader() {
    $("#Loader").attr("hidden", true);
    $("#FaceAuth").attr("hidden", false);
  }

  eel.expose(hideFaceAuth)
  function hideFaceAuth() {
    $("#FaceAuth").attr("hidden", true);
    $("#FaceAuthSuccess").attr("hidden", false);
  }

  eel.expose(hideFaceAuthSuccess)
  function hideFaceAuthSuccess() {
    $("#FaceAuthSuccess").attr("hidden", true);
    $("#HelloGreet").attr("hidden", false);
  }

  eel.expose(hideStart)
  function hideStart() {
    $("#Start").attr("hidden", true);

    setTimeout(function () {
      $("#Oval").addClass("animate__animated animate__zoomIn");
    }, 1000);

    setTimeout(function () {
      $("#Oval").attr("hidden", false);
    }, 1000);
  }
});