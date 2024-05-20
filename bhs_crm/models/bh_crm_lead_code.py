from odoo import models, fields, api, exceptions, _


class CusHrEmployee(models.Model):
    _inherit = 'hr.employee'

    def write(self, vals):
        res = super(CusHrEmployee, self).write(vals)
        if vals.get('user_id'):
            user = self.env['res.users'].browse(vals.get('user_id'))
            partner = user.partner_id
            partner.employee = True
        return res

class Lead(models.Model):
    _inherit = 'crm.lead'

    lead_code = fields.Char(string='Lead code', help="The customer code no", default='')

    @api.model
    def create(self, values):
        res = super(Lead, self).create(values)
        if not res.lead_code:
            seq_lead_code = self.env['ir.sequence'].next_by_code('lead.code')
            if seq_lead_code:
                res.lead_code = seq_lead_code

        return res

    def write(self, vals):
        for lead in self:
            if lead.lead_code == '':
                seq_lead_code = self.env['ir.sequence'].next_by_code('lead.code')
                if seq_lead_code:
                    vals['lead_code'] = seq_lead_code

        ret = super(Lead, self).write(vals)

        return ret

    @api.depends('name')
    def _compute_display_name(self):
        super()._compute_display_name()
        for lead in self:
            name = lead.display_name
            if lead.lead_code:
                name = "[%s] %s" % (lead.lead_code, name)

            lead.display_name = name.strip() if name else False

    # @api.depends('name')
    # def name_get(self):
    #     res = []
    #     for lead in self:
    #         name = lead.name
    #         if lead.lead_code:
    #             name = "[%s] %s" % (lead.lead_code, lead.name)
    #         res.append((lead.id, name))
    #     return res
