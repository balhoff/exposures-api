from flask_restplus import fields
from exposures.api.restplus import api


exposure_score = api.model('Exposure Score', {
    'id': fields.String(readOnly=True, description='Exposure unique ID'),
    'type': fields.String(readOnly=True, description='Type of association, e.g. gene-phenotype')
})
