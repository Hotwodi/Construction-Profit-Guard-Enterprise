# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgeApprovalRule(models.Model):
    _name = "cge.approval.rule"
    _description = "Approval Rule"
    _order = "sequence, name"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Rule Name",
        required=True,
        tracking=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
    )
    rule_type = fields.Selection(
        selection=[
            ("change_order", "Change Order"),
            ("budget_increase", "Budget Increase"),
            ("progress_billing", "Progress Billing"),
            ("subcontractor", "Subcontractor"),
        ],
        string="Rule Type",
        required=True,
        tracking=True,
    )
    threshold_amount = fields.Monetary(
        string="Threshold Amount",
        currency_field="currency_id",
        required=True,
        tracking=True,
        help="Amount above which approval is required.",
    )
    approver_id = fields.Many2one(
        comodel_name="res.users",
        string="Approver",
        required=True,
        tracking=True,
    )
    auto_approve_below = fields.Monetary(
        string="Auto-Approve Below",
        currency_field="currency_id",
        tracking=True,
        help="Amounts below this value are auto-approved.",
    )
    ai_risk_assessment = fields.Boolean(
        string="AI Risk Assessment",
        default=True,
        tracking=True,
        help="Enable AI-based risk assessment for this rule.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        tracking=True,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
