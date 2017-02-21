from flask_restplus import fields
from exposures.api.restplus import api


exposure_result = api.model('Exposure', {
    'stime': fields.String(readOnly=True, description='Starting time for the given measure'),
    'etime': fields.String(readOnly=True, description='Ending time for the given measure'),
    'value': fields.String(readOnly=True, description='Numerical or categorical depending upon type of value being requested'),
})
