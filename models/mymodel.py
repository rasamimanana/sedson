# -*- coding: utf-8 -*-

# 1 : imports from python lib

# 2 : imports from openerp
from openerp import models, fields, api, _
from openerp.exceptions import Warning
# 3 : imports from odoo modules

_logger = logging.getLogger(__name__)

##
## Models
##


# class mymodel(models.Model):
#     """comment ... """
#     _name = "sedson.mymodel"
#     _inherit = "..."
#
#     sprint_id = fields.Many2one('project.scrum.sprint', 'Sprint')
#     story_id = fields.Many2one('project.scrum.story', 'Story')
#     feature_id = fields.Many2one('project.scrum.feature', 'Feature')
#     date_start = fields.Datetime('Start date')
