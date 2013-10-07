<%inherit file="base.mako"/>

<%block name="header">
    <script type="text/javascript">
      var barcodeURL = "${h.barcode_scan_url(request.host_url + request.route_path('check-in', item_type_id=item_type.id))}";
      var bulkBarcodeURL = "${h.barcode_scan_url(request.host_url + request.route_path('check-in', item_type_id=item_type.id), {'bulk':'true'})}";
      var deleteURL = "${request.route_path('check-out-item', item_id='REPLACEID')}";
      var deleteTypeURL = "${request.route_path('delete-item-type', item_type_id=item_type.id)}";
    </script>
    <script type="text/javascript" src="/static/item_type.js"></script>
</%block>

  ${item_type.name} <small><i>${item_type.description}</i></small>
  There are ${len(item_type.items)} items on hand

<p>
  <a id="check-in" data-role="button" data-inline="true" href="#">Check-in</a>
  <a id="bulk-check-in" data-role="button" data-inline="true" href="#">Bulk check-in</a>
 % if len(item_type.items) == 0:
  <a id="delete-item-type" data-role="button" href="#">Delete type</a>
 % endif
</p>

  <ul data-role="listview">
    % for item in items:
      <li data-icon="delete"><a href="#" class="delete" data-id="${item.id}" data-barcode="${item.barcode}">${item.barcode} <i><small>Checked in ${h.pretty.date(item.added)}</small></i></a></li>
    % endfor
  </ul>
