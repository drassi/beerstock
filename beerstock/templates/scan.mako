<%inherit file="base.mako"/>

  Item with barcode ${item.barcode} is of type <a href="${request.route_url('item-type', item_type_id=item.item_type.id)}">${item.item_type.name}</a> <i>${item.item_type.description}</i> checked in ${h.pretty.date(item.added)}
