  function delete_item() {
    var self = $(this);
    if (confirm('Sure you want to checkout barcode ' + self.data('barcode') + '?')) {
      document.location.href = deleteURL.replace('REPLACEID', self.data('id'));
    }
  }

  $(function() {
    $('#check-in').attr('href', barcodeURL);
    $('#bulk-check-in').attr('href', bulkBarcodeURL);
    if (document.URL.indexOf('bulk=true') != -1) {
      document.location.href = bulkBarcodeURL;
    }
    $('a.delete').bind('click', delete_item);
  });
