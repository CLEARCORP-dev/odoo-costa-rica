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

from openerp import models, fields, api


class hr_employee(models.Model):

    _inherit = 'hr.employee'

    def _check_report_number_child(self, cr, uid, ids, context=None):
        for employee in self.browse(cr, uid, ids, context=context):
            if employee.report_number_child < 0:
                return False
        return True

    @api.onchange('marital')
    def _onchange_marital(self):
        self.report_spouse = False

    marital= fields.Selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')], String = 'Marital')
    report_spouse= fields.Boolean('Report Spouse', help="If this employee reports his spouse for rent payment")
    report_number_child= fields.Integer('Number of children to report', help="Number of children to report for rent payment")       

    _defaults = {
        'report_number_child': 0,
    }

    _constraints = [
        (_check_report_number_child, 'Error! The number of child to report must be greater or equal to zero.', ['report_number_child'])
    ]