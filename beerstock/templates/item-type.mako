<%inherit file="base.mako"/>

<h1>${item_type.name}: ${item_type.description}</h1>

<p>
  <a data-role="button" data-inline="true" href="#">Check-in</a>
  <a data-role="button" data-inline="true" href="#">Bulk check-in</a>
</p>

<p>
  <ul data-role="listview">
    % for item in item_type.items:
      <li data-icon="delete"><a href="#">${item.id} <i><small>Checked in ${item.added}</small></i></a></li>
    % endfor
  </ul>
</p>
