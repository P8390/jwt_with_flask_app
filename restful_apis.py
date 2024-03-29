from flask_restful import Api
from importlib import import_module
from url_list import URL_LIST


def create_restful_api(app):
    api = Api(app=app, prefix='/')
    for url_obj in URL_LIST:
        resource_name = url_obj.resource
        resource_split = resource_name.split('.')
        module_name, resource = '.'.join(resource_split[:-1]), resource_split[-1]
        try:
            imported_module = getattr(import_module(module_name), resource)
        except ImportError as exc:
            app.logger.error('module = {} can not import resource = {}'.format(module_name, resource))
            raise exc
        else:
            api.add_resource(imported_module, url_obj.url, endpoint=url_obj.name)
