from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther

from sqlalchemy.exc import DBAPIError

from .models import DBSession, ItemType, Item

from beerstock import helpers

@view_config(route_name='home', renderer='home.mako')
def home(request):
    item_types = DBSession.query(ItemType).order_by(ItemType.name).all()
    return {'item_types' : item_types}

@view_config(route_name='item-type', renderer='item-type.mako')
def item_type(request):
    item_type_id = request.matchdict['item_type_id']
    item_type = DBSession.query(ItemType).get(item_type_id)
    items = sorted(item_type.items, key=lambda item: item.added, reverse=True)
    return {'item_type' : item_type, 'items' : items}

@view_config(route_name='new-item-type', renderer='new-item-type.mako')
def new_item_type(request):
    return {}

@view_config(route_name='new-item-type-save')
def new_item_type_save(request):
    name = request.params['name']
    description = request.params['description']
    item_type = ItemType(name, description)
    DBSession.add(item_type)
    return HTTPSeeOther(location=request.route_url('home'))

@view_config(route_name='check-in')
def check_in(request):
    item_type_id = request.matchdict['item_type_id']
    item_type = DBSession.query(ItemType).get(item_type_id)
    bulk = 'bulk' in request.params
    barcode = request.params['barcode']
    item = Item(barcode, item_type)
    DBSession.add(item)
    if bulk:
        return HTTPSeeOther(location=request.route_url('item-type', item_type_id=item_type_id, _query={'bulk': 'true'}))
    else:
        return HTTPSeeOther(location=request.route_url('item-type', item_type_id=item_type_id))

@view_config(route_name='check-out-item')
def check_out_item(request):
    item_id = request.matchdict['item_id']
    item = DBSession.query(Item).get(item_id)
    DBSession.delete(item)
    return HTTPSeeOther(location=request.route_url('home'))

@view_config(route_name='check-out', renderer='check-out.mako')
def check_out(request):
    barcode = request.params['barcode']
    bulk = 'bulk' in request.params
    item = DBSession.query(Item).filter(Item.barcode==barcode).one()
    DBSession.delete(item)
    if bulk:
        return HTTPSeeOther(location=helpers.barcode_scan_url(request.host_url + request.route_path('check-out'), {'bulk':'true'}))
    else:
        return HTTPSeeOther(location=request.route_url('home'))

@view_config(route_name='scan', renderer='scan.mako')
def scan(request):
    barcode = request.params['barcode']
    item = DBSession.query(Item).filter(Item.barcode==barcode).one()
    return {'item' : item}

@view_config(route_name='delete-item-type')
def delete_item_type(request):
    item_type_id = request.matchdict['item_type_id']
    item_type = DBSession.query(ItemType).get(item_type_id)
    if len(item_type.items) > 0:
        raise Exception('must be empty')
    DBSession.delete(item_type)
    return HTTPSeeOther(location=request.route_url('home'))

@view_config(route_name='rate-beer-scan')
def rate_beer_scan(request):
    return HTTPSeeOther(location='zxing://scan/?ret=http%3A%2F%2Fwww.ratebeer.com%2Fjson%2Fw_upc.asp%3Fupc%3D%7BCODE%7D')
