# -*- encoding: utf-8 -*-
from osv import osv, fields

class bac_clientid(osv.osv):
    """
    Record to hold the BACNet Client ID for the company.
    """
    _name = 'banking.bac.clientid'
    _description = 'BAC Client ID'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'clientid': fields.char('Client ID', size=20, required=True),
        'company_id': fields.many2one('res.company','Company', required=True),
        }

    _defaults = {
        'company_id': lambda self,cr,uid,c: self.pool.get('res.users').browse(cr, uid, uid, c).company_id.id,
        }
    
bac_clientid()


class payment_order(osv.osv):
    _name = 'payment.order'
    _inherit = 'payment.order'

    _columns = {
        'bac_clientid_id': fields.many2one('banking.bac.clientid', 'BAC Client ID', required=True),
        }


    def _default_bac_clientid(self, cr, uid, context=None):
        company_id = self.pool.get('res.users').browse(cr, uid, uid, context=context).company_id.id
        
        clientid_ids = self.pool.get('banking.bac.clientid').search(cr, uid, [('company_id','=',company_id)])
        if len(clientid_ids)==0:
            return False
        else:
            return clientid_ids[0]


    _defaults = {
         'bac_clientid_id':_default_bac_clientid,
        }

payment_order()

