# -*- coding: utf-8 -*-
{
    "name": "Construction Profit Guard Enterprise: Subcontractor Portal, "
            "Forecasting & Portfolio Reporting",
    "version": "18.0.1.0.0",
    'images': ['static/description/cover.png'],
    "summary": "Executive portfolio dashboard, AI margin forecasting, "
               "subcontractor portal, approval rules, document extraction "
               "and cost code budget alerts for construction enterprises.",
    "description": """
Construction Profit Guard Enterprise
=====================================

Executive portfolio dashboard, AI-powered margin at completion forecasting,
subcontractor portal with approval workflows, automated document extraction,
and cost code budget alerts — all in one integrated Odoo module for
construction enterprises.

Key Features
------------
* Portfolio Dashboard — executive-level visibility across all projects
* Margin Forecasts — AI-driven margin at completion predictions
* Subcontractor Portal — controlled access for subcontractors with approvals
* Approval Rules — configurable thresholds with AI risk assessment
* Document Extraction — automated AI extraction of bids, change orders, invoices
* Cost Code Alerts — proactive budget threshold and overrun alerts
""",
    "author": "SoftaiDev",
    "website": "https://softaidev.pages.dev",
    "category": "Productivity/AI",
    "license": "LGPL-3",
    "price": 1499.99,
    "currency": "USD",
    "application": True,
    "installable": True,
    "depends": [
        "base",
        "web",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/portfolio_dashboard_views.xml",
        "views/margin_forecast_views.xml",
        "views/subcontractor_portal_views.xml",
        "views/approval_rule_views.xml",
        "views/document_extraction_views.xml",
        "views/cost_code_alert_views.xml",
        "views/menu.xml",
    ],
}
