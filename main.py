from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from sse_starlette.sse import EventSourceResponse
import asyncio
import datetime
import json

app = FastAPI()

@app.get("/")
async def root():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>SSE Demo</title>
        </head>
        <body>
            <h1>Server-Sent Events Demo</h1>
            <div id="events"></div>

            <script>
                const eventsDiv = document.getElementById('events');
                const eventSource = new EventSource('/stream');

                eventSource.onmessage = function(event) {
                    const newElement = document.createElement('div');
                    try {
                        const eventData = JSON.parse(event.data);
                        newElement.textContent = `Count: ${eventData.count} - Time: ${eventData.time}`;
                        eventsDiv.prepend(newElement);
                    } catch (error) {
                        console.error('Failed to parse event data:', error);
                        newElement.textContent = `Raw data: ${event.data}`;
                        eventsDiv.prepend(newElement);
                    }
                };

                eventSource.onerror = function(error) {
                    console.error('EventSource failed:', error);
                    eventSource.close();
                };
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

async def event_generator():
    count = 0
    while True:
        count += 1
        data = {
            "count": count,
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        }
        yield {
            "data": json.dumps(data)  # Properly serialize the data to JSON
        }
        await asyncio.sleep(1)

@app.get('/stream')
async def message_stream(request: Request):
    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 