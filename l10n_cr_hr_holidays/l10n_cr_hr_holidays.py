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
from openerp.osv import osv, fields

class hr_employee(osv.Model):
    
    def add_legal_leaves_per_period(self, cr, uid, ids=[], context={}):
        if not ids:
            ids = self.search(cr, uid, [], context=context)
        employees = self.browse(cr, uid, ids, context=context)
        for employee_obj in employees:
            sum = employee_obj.remaining_leaves + employee_obj.leaves_per_period
            self.write(cr, uid, employee_obj.id, {'remaining_leaves': sum}, context=context)
    
    _inherit="hr.employee"
    
    _columns= {
               'leaves_per_period': fields.float(string='Legal Leaves per Period',
                                                 help='Total number of legal leaves to be added to this employee per period.')
               }
