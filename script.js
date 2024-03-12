function sendMessage() {
    var input = document.getElementById("input");
    var message = input.value.trim();
    if (message !== "") {
      var chatBox = document.getElementById("chat-box");
      var newMessage = document.createElement("div");
      newMessage.classList.add("chat-message");
      newMessage.innerText = message;
      chatBox.appendChild(newMessage);
      input.value = "";
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
  