# -*- coding: utf-8 -*-

from odoo import models, api, fields
from datetime import datetime


class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    
    short_codes = fields.Char(string="Short Codes")