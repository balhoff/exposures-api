import logging

from flask import request
from flask_restplus import Resource
from exposures.datamodel.serializers import exposure_result
from exposures.api.restplus import api
import pysolr

log = logging.getLogger(__name__)

ns = api.namespace('exposure', description='Exposure scores and raw values for a time and place')

value_parser = api.parser()
value_parser.add_argument('stime', type='string', help="The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored.", location='query', required=True)
value_parser.add_argument('etime', type='string', help="The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored.", location='query', required=True)
value_parser.add_argument('loc', type='string', help="""A description of the location(s) to retrieve the exposure for. Locaton may be a single 
            geocoordinate (example '35.720278,-79.176389') or a semicomma separated list of geocoord:dayhours 
            giving the start and ending hours on specific days of the week at that location 
            (example '35.720278,-79.176389,Sa0813;35.720278,-79.176389,other') indicates Saturdays from 8am 
            to 1pm is at one location and all other times are at another location. Hours should be in 24 hours 
            time using 2 digits, days of the week should be the first two characters of the day.If the day of 
            the week does not appear then the time periods apply to all days 
            (example '35.720278,-79.176389,0614,35.731944,-78.852778,1424') gives two time periods for all days. 
            If hours do not appear then the time period applies to all hours of the day 
            (example '35.720278,-79.176389,Sa,35.731944,-78.852778,Su').""", location='query', required=True)
value_parser.add_argument('tres', type='string', help="The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'", location='query', required=False)
value_parser.add_argument('tstat', type='string', help="The statistic to use for results, should be one of 'max', 'mean', or 'median'. Default is 'max'", location='query', required=False)

score_parser = api.parser()
score_parser.add_argument('stime', type='string', help="The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored.", location='query', required=True)
score_parser.add_argument('etime', type='string', help="The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored.", location='query', required=True)
score_parser.add_argument('loc', type='string', help="""A description of the location(s) to retrieve the exposure for. Locaton may be a single 
            geocoordinate (example '35.720278,-79.176389') or a semicomma separated list of geocoord:dayhours 
            giving the start and ending hours on specific days of the week at that location 
            (example '35.720278,-79.176389,Sa0813;35.720278,-79.176389,other') indicates Saturdays from 8am 
            to 1pm is at one location and all other times are at another location. Hours should be in 24 hours 
            time using 2 digits, days of the week should be the first two characters of the day.If the day of 
            the week does not appear then the time periods apply to all days 
            (example '35.720278,-79.176389,0614,35.731944,-78.852778,1424') gives two time periods for all days. 
            If hours do not appear then the time period applies to all hours of the day 
            (example '35.720278,-79.176389,Sa,35.731944,-78.852778,Su').""", location='query', required=True)
score_parser.add_argument('tres', type='string', help="The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'", location='query', required=False)
score_parser.add_argument('tscore', type='string', help="The exposure score type to return. The accepted values vary by exposure factor. For pm2.5 values are '7dayrisk', '14dayrisk' (NOT COMPLETE)", location='query', required=False)

@ns.route('/exposureValue/<exposure>')
@api.param('exposure', "The name of the exposure factor (currently limited to pm2.5, ozone).")
class ExposureQuery(Resource):

    @api.expect(value_parser)
    @api.marshal_list_with(exposure_result)
    @api.doc(id='getExposureValue', description="Retrieve the computed exposure value for a given environmental exposure factor, time period, and set of locations.")
    def get(self, query):
        """
        Get exposure value for a given environmental factor
        """
        args = parser.parse_args()
        return []


@ns.route('/exposureScore/<exposure>')
class ExposureQuery(Resource):

    @api.expect(score_parser)
    @api.marshal_list_with(exposure_result)
    @api.doc(id='getExposureScore', description="Retrieve the computed exposure score for a given environmental exposure factor, time period, and set of locations.")
    def get(self, query):
        """
        Get exposure score for a given environmental factor
        """
        args = parser.parse_args()
        return []
