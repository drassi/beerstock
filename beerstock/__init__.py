from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid.events import BeforeRender
from beerstock import helpers

from .models import (
    DBSession,
    Base,
    )

def add_renderer_globals(event):
    event['h'] = helpers

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('item-type', '/item/{item_type_id}')
    config.add_route('new-item-type', '/new-type')
    config.add_route('new-item-type-save', '/new-type/save')
    config.add_route('check-in', '/check-in/{item_type_id}')
    config.add_route('check-out-item', '/check-out/item/{item_id}')
    config.add_route('check-out', '/check-out/barcode')
    config.add_route('scan', '/scan')
    config.add_route('delete-item-type', '/delete-type/{item_type_id}')
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.scan()
    return config.make_wsgi_app()
