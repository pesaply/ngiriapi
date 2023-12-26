
ngiriapi includes an application class `ngiriapi` that nicely ties together all of
its other functionality.

```python
from ngiriapi.applications import ngiriapi
from ngiriapi.responses import PlainTextResponse
from ngiriapi.routing import Route, Mount, WebSocketRoute
from ngiriapi.staticfiles import StaticFiles


def homepage(request):
    return PlainTextResponse('Hello, world!')

def user_me(request):
    username = "John Doe"
    return PlainTextResponse('Hello, %s!' % username)

def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()

def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
    Route('/user/me', user_me),
    Route('/user/{username}', user),
    WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory="static")),
]

app = ngiriapi(debug=True, routes=routes, on_startup=[startup])
```

### Instantiating the application

::: ngiriapi.applications.ngiriapi
    :docstring:

### Storing state on the app instance

You can store arbitrary extra state on the application instance, using the
generic `app.state` attribute.

For example:

```python
app.state.ADMIN_EMAIL = 'admin@example.org'
```

### Accessing the app instance

Where a `request` is available (i.e. endpoints and middleware), the app is available on `request.app`.
