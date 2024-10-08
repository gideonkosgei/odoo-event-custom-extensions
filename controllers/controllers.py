from odoo import http
from odoo.http import request
from werkzeug.utils import redirect  # Import redirect

class BarcodeSearchController(http.Controller):

    # Update the route to accept a barcode as a URL parameter
    @http.route('/web/barcode_search/barcode/<string:barcode>', type='http', auth='public', methods=['GET'],
                website=True)
    def barcode_search(self, barcode):
        # Search for the record using the barcode
        record = request.env['event.voucher'].search([('barcode', '=', barcode)], limit=1)

        if record:
            # Redirect to the form view of the found record
            return redirect('/web#id=%s&model=event.voucher&view_type=form' % record.id)
        else:
            return "Record not found"
