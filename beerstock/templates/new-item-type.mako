<%inherit file="base.mako"/>

<form action="${request.route_path('new-item-type-save')}" method="post">
  <label for="name">Name</label>
  <input type="text" data-clear-btn="true" name="name" id="name" value="">
  <label for="description">Description</label>
  <input type="text" data-clear-btn="true" name="description" id="description" value="">
  <input type="submit" value="Save">
</form>
