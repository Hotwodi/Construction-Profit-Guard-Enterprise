# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CgeDocumentExtraction(models.Model):
    _name = "cge.document.extraction"
    _description = "Document Extraction Queue"
    _order = "create_date desc"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Reference",
        required=True,
        tracking=True,
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        tracking=True,
    )
    document_type = fields.Selection(
        selection=[
            ("bid", "Bid"),
            ("change_order", "Change Order"),
            ("invoice", "Invoice"),
            ("co_insurance", "COI / Insurance"),
            ("delivery_ticket", "Delivery Ticket"),
        ],
        string="Document Type",
        required=True,
        tracking=True,
    )
    file_name = fields.Char(
        string="File Name",
        tracking=True,
    )
    extraction_status = fields.Selection(
        selection=[
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
        string="Extraction Status",
        default="pending",
        required=True,
        tracking=True,
    )
    extracted_data = fields.Text(
        string="Extracted Data",
        help="JSON or text data extracted by the AI engine.",
    )
    ai_confidence = fields.Float(
        string="AI Confidence (%)",
        digits=(6, 2),
        tracking=True,
    )
    reviewed = fields.Boolean(
        string="Reviewed",
        default=False,
        tracking=True,
    )
    reviewed_by = fields.Many2one(
        comodel_name="res.users",
        string="Reviewed By",
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    def action_start_processing(self):
        for rec in self:
            rec.extraction_status = "processing"

    def action_mark_completed(self):
        for rec in self:
            rec.extraction_status = "completed"

    def action_mark_failed(self):
        for rec in self:
            rec.extraction_status = "failed"

    def action_mark_reviewed(self):
        for rec in self:
            rec.reviewed = True
            rec.reviewed_by = self.env.user
