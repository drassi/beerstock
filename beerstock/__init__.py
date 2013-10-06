from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


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
    config.add_route('check-out', '/check-out/{item_id}')
    config.scan()
    return config.make_wsgi_app()
