<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/jquery-mobile/1.3.2/jquery.mobile.min.css" />
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery-mobile/1.3.2/jquery.mobile.min.js"></script>
    <script type="text/javascript">
      $(function() {
        var scan = document.getElementById('scan');
        var extra = '&';
        if (document.URL.indexOf('?') == -1) {
          extra = '?';
        }
        scan.href = 'zxing://scan/?ret=' + encodeURIComponent(document.URL + extra + 'code={CODE}');
        //document.location.href = scan.href;
      });
    </script>
  </head>
  <body>
    <div data-role="page">
      <div data-role="header" data-position="fixed">
        <div data-role="navbar">
          <ul>
            <li><a href="${request.route_path('home')}">Home</a></li>
            <li><a href="#">Scan</a></li>
            <li><a href="#">Checkout</a></li>
            <li><a href="#">Bulk checkout</a></li>
          </ul>
        </div>
      </div>
      <div data-role="content">
        ${self.body()}
      </div>
    </div>
  </body>
</html>
