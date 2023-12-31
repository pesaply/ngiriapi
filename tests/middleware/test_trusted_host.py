from ngiriapi.applications import ngiriapi
from ngiriapi.middleware import Middleware
from ngiriapi.middleware.trustedhost import TrustedHostMiddleware
from ngiriapi.responses import PlainTextResponse
from ngiriapi.routing import Route


def test_trusted_host_middleware(test_client_factory):
    def homepage(request):
        return PlainTextResponse("OK", status_code=200)

    app = ngiriapi(
        routes=[Route("/", endpoint=homepage)],
        middleware=[
            Middleware(
                TrustedHostMiddleware, allowed_hosts=["testserver", "*.testserver"]
            )
        ],
    )

    client = test_client_factory(app)
    response = client.get("/")
    assert response.status_code == 200

    client = test_client_factory(app, base_url="http://subdomain.testserver")
    response = client.get("/")
    assert response.status_code == 200

    client = test_client_factory(app, base_url="http://invalidhost")
    response = client.get("/")
    assert response.status_code == 400


def test_default_allowed_hosts():
    app = ngiriapi()
    middleware = TrustedHostMiddleware(app)
    assert middleware.allowed_hosts == ["*"]


def test_www_redirect(test_client_factory):
    def homepage(request):
        return PlainTextResponse("OK", status_code=200)

    app = ngiriapi(
        routes=[Route("/", endpoint=homepage)],
        middleware=[
            Middleware(TrustedHostMiddleware, allowed_hosts=["www.example.com"])
        ],
    )

    client = test_client_factory(app, base_url="https://example.com")
    response = client.get("/")
    assert response.status_code == 200
    assert response.url == "https://www.example.com/"
