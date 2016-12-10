from cornice.service import get_services
from cornice_swagger.swagger import generate_swagger_spec
from pyramid.security import NO_PERMISSION_REQUIRED
from kinto.core import logger


def swagger(request):
    return {"request": request}


def swagger_json(request):
    info = {"title": "Joes API", "version": "0.1", "contact": {
            "name": "Joe Smith",
            "email": "joe.cool@swagger.com"}
            }
    base_path = "/"
    services = get_services()
    spec = generate_swagger_spec(services, info["title"],
                                 info["version"], info=info,
                                 base_path=base_path, head=False)
    logger.info(spec)
    return spec


def includeme(config):
    config.include("pyramid_chameleon")
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("swagger", "/swagger")
    config.add_route("swagger_json", "/swagger_json")
    config.add_view(swagger, route_name="swagger", renderer="templates/index.pt",
                    permission=NO_PERMISSION_REQUIRED)
    config.add_view(swagger_json, route_name="swagger_json", renderer="json",
                    permission=NO_PERMISSION_REQUIRED)
    config.add_api_capability(
        "swagger",
        description="The swagger api docu",
        url="https://kinto.readthedocs.io/en/latest/api/1.x/"
            "swagger.html")
