# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgeSubcontractorPortal(models.Model):
    _name = "cge.subcontractor.portal"
    _description = "Subcontractor Portal Access"
    _order = "name"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Portal Name",
        required=True,
        tracking=True,
    )
    vendor_id = fields.Many2one(
        comodel_name="res.partner",
        string="Subcontractor / Vendor",
        required=True,
        tracking=True,
        domain="[('is_company', '=', True)]",
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        tracking=True,
    )
    access_level = fields.Selection(
        selection=[
            ("full", "Full Access"),
            ("limited", "Limited Access"),
            ("read_only", "Read Only"),
        ],
        string="Access Level",
        default="read_only",
        required=True,
        tracking=True,
    )
    approved_work_orders = fields.Integer(
        string="Approved Work Orders",
        tracking=True,
    )
    pending_approvals = fields.Integer(
        string="Pending Approvals",
        tracking=True,
    )
    document_count = fields.Integer(
        string="Document Count",
        tracking=True,
    )
    last_login = fields.Datetime(
        string="Last Login",
        tracking=True,
    )
    state = fields.Selection(
        selection=[
            ("active", "Active"),
            ("inactive", "Inactive"),
        ],
        string="State",
        default="active",
        required=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    def action_activate(self):
        for rec in self:
            rec.state = "active"

    def action_deactivate(self):
        for rec in self:
            rec.state = "inactive"
