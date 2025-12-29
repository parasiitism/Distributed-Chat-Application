
const username = "user1";
const ws = new WebSocket(`ws://localhost:8000/ws/${username}`);

ws.onmessage = (event) => {
  const li = document.createElement("li");
  li.innerText = event.data;
  document.getElementById("messages").appendChild(li);
};

function sendMessage() {
  const input = document.getElementById("message");
  ws.send(input.value);
  input.value = "";
}
