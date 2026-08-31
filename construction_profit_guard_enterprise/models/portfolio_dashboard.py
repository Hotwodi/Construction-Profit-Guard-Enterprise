# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgePortfolioDashboard(models.Model):
    _name = "cge.portfolio.dashboard"
    _description = "Executive Portfolio Dashboard"
    _order = "create_date desc"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Dashboard Name",
        required=True,
        tracking=True,
    )
    period = fields.Char(
        string="Period",
        required=True,
        help="Reporting period, e.g. '2025-Q1' or 'January 2025'.",
    )
    total_projects = fields.Integer(
        string="Total Projects",
        tracking=True,
    )
    active_projects = fields.Integer(
        string="Active Projects",
        tracking=True,
    )
    total_contract_value = fields.Monetary(
        string="Total Contract Value",
        currency_field="currency_id",
        tracking=True,
    )
    total_budget = fields.Monetary(
        string="Total Budget",
        currency_field="currency_id",
        tracking=True,
    )
    total_committed = fields.Monetary(
        string="Total Committed Cost",
        currency_field="currency_id",
        tracking=True,
    )
    total_incurred = fields.Monetary(
        string="Total Incurred Cost",
        currency_field="currency_id",
        tracking=True,
    )
    total_billed = fields.Monetary(
        string="Total Billed",
        currency_field="currency_id",
        tracking=True,
    )
    portfolio_margin = fields.Float(
        string="Portfolio Margin (%)",
        digits=(6, 2),
        tracking=True,
        help="Overall portfolio margin percentage.",
    )
    ai_forecast_accuracy = fields.Float(
        string="AI Forecast Accuracy (%)",
        digits=(6, 2),
        tracking=True,
        help="Accuracy of AI margin forecasts across the portfolio.",
    )
    at_risk_projects = fields.Integer(
        string="At-Risk Projects",
        tracking=True,
        help="Number of projects flagged as at-risk by the AI engine.",
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

    @api.depends("total_contract_value", "total_incurred")
    def _compute_portfolio_margin(self):
        for rec in self:
            if rec.total_contract_value and rec.total_incurred:
                rec.portfolio_margin = (
                    (rec.total_contract_value - rec.total_incurred)
                    / rec.total_contract_value
                    * 100.0
                )
            else:
                rec.portfolio_margin = 0.0
