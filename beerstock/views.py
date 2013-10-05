from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import DBSession, ItemType, Item

@view_config(route_name='home', renderer='home.mako')
def home(request):
    item_types = DBSession.query(ItemType).all()
    return {'item_types' : item_types}

@view_config(route_name='item-type', renderer='item-type.mako')
def item_type(request):
    item_type_id = request.matchdict['item_type_id']
    item_type = DBSession.query(ItemType).get(item_type_id)
    return {'item_type' : item_type}
