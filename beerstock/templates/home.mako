<%inherit file="base.mako"/>

<%block name="header">
  <h1>Home</h1>
</%block>

<p>
  <a id="scan" data-role="button" href="#">Info</a>
  <a id="scan" data-role="button" href="#">Check-out</a>
</p>

<p>
  <ul data-role="listview" data-filter="true">
    % for item_type in item_types:
      <li><a href="${request.route_path('item-type', item_type_id=item_type.id)}">${item_type.name} <i><small>${item_type.description}</small></i><span class="ui-li-count">${len(item_type.items)}</span></a></li>
    % endfor
  </ul>
</p>
