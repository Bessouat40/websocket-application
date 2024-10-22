const counter: HTMLParagraphElement = document.createElement('p');
const ws: WebSocket = new WebSocket('ws://localhost:8000');
ws.onmessage = (event: MessageEvent) => {
  counter.textContent = event.data + 's have passed...';
};
document.body.appendChild(counter);
