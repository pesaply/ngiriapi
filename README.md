<p align="center">
 
</p>
<p align="center">
    <em>✨ The Smalest ASGI framework for python ✨</em>
</p>
<p align="center">

</p>

---

**Documentation**: [https://www.ngiri.co.tz/](https://www.ngiri.co.tz/)

---

# ngiriapi

Ngiriapi is a lightweight [ASGI][asgi] framework/toolkit,
which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

* A lightweight, low-complexity HTTP web framework.
* WebSocket support.
* In-process background tasks.
* Startup and shutdown events.
* Test client built on `httpx`.
* CORS, GZip, Static Files, Streaming responses.
* Session and Cookie support.
* 100% test coverage.
* 100% type annotated codebase.
* Few hard dependencies.
* Compatible with `asyncio` and `trio` backends.
* Great overall performance [against independent benchmarks][techempower].

## Requirements

Python 3.8+

## Installation

```shell
$ pip3 install ngiriapi
```

You'll also want to install an ASGI server, such as [uvicorn](http://www.uvicorn.org/), [daphne](https://github.com/django/daphne/), or [hypercorn](https://pgjones.gitlab.io/hypercorn/).

```shell
$ pip3 install uvicorn
```

## Example

**example.py**:

```python
from ngiriapi.applications import ngiriapi
from ngiriapi.responses import JSONResponse
from ngiriapi.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", endpoint=homepage)
]

app = ngiriapi(debug=True, routes=routes)
```

Then run the application using Uvicorn:

```shell
$ uvicorn example:app
```

For a more complete example, see [pesaply/ngiriapi-example](https://github.com/pesaply/ngiriapi-example).

## Dependencies

ngiriapi only requires `anyio`, and the following are optional:

* [`ngiri`][ngiri] - Required if you want to use the `TestClient`.
* [`jinja2`][jinja2] - Required if you want to use `Jinja2Templates`.
* [`python-multipart`][python-multipart] - Required if you want to support form parsing, with `request.form()`.
* [`itsdangerous`][itsdangerous] - Required for `SessionMiddleware` support.
* [`pyyaml`][pyyaml] - Required for `SchemaGenerator` support.

You can install all of these with `pip3 install ngiriapi[full]`.

## Framework or Toolkit

ngiriapi is designed to be used either as a complete framework, or as
an ASGI toolkit. You can use any of its components independently.

```python
from ngiriapi.responses import PlainTextResponse


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)
```

Run the `app` application in `example.py`:

```shell
$ uvicorn example:app
INFO: Started server process [11509]
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Run uvicorn with `--reload` to enable auto-reloading on code changes.

## Modularity

The modularity that ngiriapi is designed on promotes building re-usable
components that can be shared between any ASGI framework. This should enable
an ecosystem of shared middleware and mountable applications.

The clean API separation also means it's easier to understand each component
in isolation.

---


[asgi]: https://asgi.readthedocs.io/en/latest/
[ngiri]: https://www.ngiri.co.tz/
[jinja2]: https://jinja.palletsprojects.com/
[python-multipart]: https://andrew-d.github.io/python-multipart/
[itsdangerous]: https://itsdangerous.palletsprojects.com/
[sqlalchemy]: https://www.sqlalchemy.org
[pyyaml]: https://pyyaml.org/wiki/PyYAMLDocumentation
[techempower]: https://www.techempower.com/benchmarks/#hw=ph&test=fortune&l=zijzen-sf
