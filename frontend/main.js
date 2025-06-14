$(document).ready(function () {
  $('.text').textillate({
    loop: true,
    sync: true,
    in: {
      effect: 'bounceIn'
    },
    out: {
      effect: 'bounceOut'
    }
  });

  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    autostart: true
  });

  $('.siri-message').textillate({
    loop: true,
    sync: true,
    in: {
      effect: 'fadeInUp',
      sync: true
    },
    out: {
      effect: 'fadeOutUp',
      sync: true
    }
  });

  $('#MicBtn').click(function () {
    eel.assistant_sound();
    $('#Oval').attr("hidden", true);
    $('#SiriWave').attr("hidden", false);
    eel.all_commands()();
  });

  // Adding the shortcut key
  function docKeyUp(e) {
    if (e.key === 'j' && e.metaKey) {
      eel.assistant_sound();
      $('#Oval').attr("hidden", true);
      $('#SiriWave').attr("hidden", false);
      eel.all_commands()();
    }
  }
  document.addEventListener('keyup', docKeyUp, false);

  function playAssistant(message) {
    if (message != "") {
      $('#Oval').attr("hidden", true);
      $('#SiriWave').attr("hidden", false);
      eel.all_commands(message);
      $('#chatbox').val("");
      $('#MicBtn').attr("hidden", false);
      $('#SendBtn').attr("hidden", true);
    }
  }

  function ShowHideButton(message) {
    if (message.length == 0) {
      $('#MicBtn').attr("hidden", false);
      $('#SendBtn').attr("hidden", true);
    } else {
      $('#MicBtn').attr("hidden", true);
      $('#SendBtn').attr("hidden", false);
    }
  }

  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message);
  });

  $("#SendBtn").click(function () {
    let message = $("#chatbox").val();
    playAssistant(message);
  });

  // To make work when we press Enter
  $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
      let message = $("#chatbox").val();
      playAssistant(message);
    }
  });
});