from ngiriapi.applications import ngiriapi
from ngiriapi.middleware import Middleware
from ngiriapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from ngiriapi.responses import PlainTextResponse
from ngiriapi.routing import Route


def test_https_redirect_middleware(test_client_factory):
    def homepage(request):
        return PlainTextResponse("OK", status_code=200)

    app = ngiriapi(
        routes=[Route("/", endpoint=homepage)],
        middleware=[Middleware(HTTPSRedirectMiddleware)],
    )

    client = test_client_factory(app, base_url="https://testserver")
    response = client.get("/")
    assert response.status_code == 200

    client = test_client_factory(app)
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://testserver/"

    client = test_client_factory(app, base_url="http://testserver:80")
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://testserver/"

    client = test_client_factory(app, base_url="http://testserver:443")
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://testserver/"

    client = test_client_factory(app, base_url="http://testserver:123")
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://testserver:123/"
