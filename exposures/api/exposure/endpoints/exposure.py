import logging

from flask import request
from flask_restplus import Resource
from exposures.datamodel.serializers import exposure_score
from exposures.api.restplus import api
import pysolr

log = logging.getLogger(__name__)

ns = api.namespace('exposure', description='foo bar')

@ns.route('/score/<query>')
class ExposureQuery(Resource):

    @api.marshal_list_with(exposure_score)
    def get(self, query):
        """
        Returns a list of scores
        """
        args = parser.parse_args()
        return []
