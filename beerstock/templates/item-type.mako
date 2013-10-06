<%inherit file="base.mako"/>

<%block name="header">
    <script type="text/javascript">
      var barcodeURL = "zxing://scan/?ret=" + encodeURIComponent("${request.host_url}${request.route_path('check-in', item_type_id=item_type.id)}?barcode={CODE}");
      var bulkBarcodeURL = barcodeURL + encodeURIComponent("&bulk=true");
      var deleteURL = "${request.route_path('check-out', item_id='REPLACEID')}";
    </script>
    <script type="text/javascript" src="/static/item_type.js"></script>
</%block>

  ${item_type.name} <small><i>${item_type.description}</i></small>
  There are ${len(item_type.items)} items on hand

<p>
  <a id="check-in" data-role="button" data-inline="true" href="#">Check-in</a>
  <a id="bulk-check-in" data-role="button" data-inline="true" href="#">Bulk check-in</a>
</p>

  <ul data-role="listview">
    % for item in items:
      <li data-icon="delete"><a href="#" class="delete" data-id="${item.id}" data-barcode="${item.barcode}">${item.barcode} <i><small>Checked in ${pretty.date(item.added)}</small></i></a></li>
    % endfor
  </ul>
