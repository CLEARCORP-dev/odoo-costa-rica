# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv

class l10n_cr_AccountFinancialReportWizard( osv.osv_memory ):

    _inherit = "accounting.report"
    _name = "accounting.report"

    def _print_report( self, cr, uid, ids, data, context = None ):
        data['form'].update( self.read( cr, uid, ids, ['date_from_cmp', 'debit_credit', 'date_to_cmp', 'fiscalyear_id_cmp', 'period_from_cmp', 'period_to_cmp', 'filter_cmp', 'account_report_id', 'enable_filter', 'label_filter'], context = context )[0] )
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'account_financial_report_webkit',
            'datas': data,
        }


