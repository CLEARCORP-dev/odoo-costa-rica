# -*- coding: utf-8 -*-
# © 2016 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv import fields, osv


class res_partner(osv.osv):

    _inherit = 'res.partner'

    _columns = {
        'adime_id': fields.many2one('adime.assigned', 'Porcentaje Adime'),
        'is_adime': fields.boolean('Socio Adime'),
    }
