import urllib

import pretty

ZXING_SCAN_BASE_URL = "zxing://scan/?"

def barcode_scan_url(url, p={}):
    params = ('&' + urllib.urlencode(p)) if p else ''
    return ZXING_SCAN_BASE_URL + urllib.urlencode({'ret' : url + '?barcode={CODE}' + params})
