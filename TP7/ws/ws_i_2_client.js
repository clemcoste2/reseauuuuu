async function hello() {
    const uri = "ws://localhost:8765";
    const websocket = new WebSocket(uri);

    websocket.onopen = function(event) {
        const name = prompt("What's your name? ");

        websocket.send(name);
        console.log(`>>> ${name}`);
    };

    websocket.onmessage = function(event) {
        const greeting = event.data;
        console.log(`<<< ${greeting}`);
        websocket.close(); // Close the connection after receiving a response
    };
}

hello();
