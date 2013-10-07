  function delete_item() {
    var self = $(this);
    if (confirm('Sure you want to checkout barcode ' + self.data('barcode') + '?')) {
      document.location.href = deleteURL.replace('REPLACEID', self.data('id'));
    }
  }

  function delete_item_type() {
    if (confirm('Sure you want to delete this type?')) {
      document.location.href = deleteTypeURL;
    }
  }

  $(function() {
    $('#check-in').attr('href', barcodeURL);
    $('#bulk-check-in').attr('href', bulkBarcodeURL);
    if (document.URL.indexOf('bulk=true') != -1) {
      document.location.href = bulkBarcodeURL;
    }
    $('a.delete').click(delete_item);
    $('#delete-item-type').click(delete_item_type);
  });
