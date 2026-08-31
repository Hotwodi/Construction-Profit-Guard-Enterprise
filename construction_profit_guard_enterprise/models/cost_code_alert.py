# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgeCostCodeAlert(models.Model):
    _name = "cge.cost.code.alert"
    _description = "Cost Code Budget Alert"
    _order = "triggered_date desc"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Alert Name",
        required=True,
        tracking=True,
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        tracking=True,
    )
    cost_code_id = fields.Char(
        string="Cost Code",
        required=True,
        tracking=True,
        help="Identifier of the cost code being monitored.",
    )
    alert_type = fields.Selection(
        selection=[
            ("budget_threshold", "Budget Threshold"),
            ("committed_exceeded", "Committed Exceeded"),
            ("overrun_predicted", "Overrun Predicted"),
        ],
        string="Alert Type",
        required=True,
        tracking=True,
    )
    threshold_pct = fields.Float(
        string="Threshold (%)",
        digits=(6, 2),
        tracking=True,
    )
    current_pct = fields.Float(
        string="Current (%)",
        digits=(6, 2),
        tracking=True,
    )
    ai_severity = fields.Selection(
        selection=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
            ("critical", "Critical"),
        ],
        string="AI Severity",
        default="low",
        tracking=True,
    )
    state = fields.Selection(
        selection=[
            ("active", "Active"),
            ("acknowledged", "Acknowledged"),
            ("resolved", "Resolved"),
        ],
        string="State",
        default="active",
        required=True,
        tracking=True,
    )
    triggered_date = fields.Datetime(
        string="Triggered Date",
        default=fields.Datetime.now,
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    def action_acknowledge(self):
        for rec in self:
            rec.state = "acknowledged"

    def action_resolve(self):
        for rec in self:
            rec.state = "resolved"

    def action_reactivate(self):
        for rec in self:
            rec.state = "active"
