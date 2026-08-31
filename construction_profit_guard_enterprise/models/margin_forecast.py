# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgeMarginForecast(models.Model):
    _name = "cge.margin.forecast"
    _description = "Margin at Completion Forecast"
    _order = "last_updated desc"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Forecast Reference",
        required=True,
        tracking=True,
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        tracking=True,
    )
    contract_value = fields.Monetary(
        string="Contract Value",
        currency_field="currency_id",
        tracking=True,
    )
    budget = fields.Monetary(
        string="Budget",
        currency_field="currency_id",
        tracking=True,
    )
    committed_cost = fields.Monetary(
        string="Committed Cost",
        currency_field="currency_id",
        tracking=True,
    )
    incurred_cost = fields.Monetary(
        string="Incurred Cost",
        currency_field="currency_id",
        tracking=True,
    )
    completion_pct = fields.Float(
        string="Completion (%)",
        digits=(6, 2),
        tracking=True,
    )
    forecast_cost_at_completion = fields.Monetary(
        string="Forecast Cost at Completion",
        currency_field="currency_id",
        tracking=True,
    )
    forecast_margin = fields.Float(
        string="Forecast Margin (%)",
        digits=(6, 2),
        tracking=True,
    )
    ai_confidence = fields.Float(
        string="AI Confidence (%)",
        digits=(6, 2),
        tracking=True,
        help="Confidence score of the AI forecast (0-100).",
    )
    trend = fields.Selection(
        selection=[
            ("improving", "Improving"),
            ("stable", "Stable"),
            ("declining", "Declining"),
        ],
        string="Trend",
        default="stable",
        tracking=True,
    )
    last_updated = fields.Datetime(
        string="Last Updated",
        default=fields.Datetime.now,
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

    @api.onchange("contract_value", "forecast_cost_at_completion")
    def _onchange_forecast_margin(self):
        for rec in self:
            if rec.contract_value and rec.forecast_cost_at_completion:
                rec.forecast_margin = (
                    (rec.contract_value - rec.forecast_cost_at_completion)
                    / rec.contract_value
                    * 100.0
                )
            else:
                rec.forecast_margin = 0.0
