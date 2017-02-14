import logging.config

from flask import Flask, Blueprint
from flask_cors import CORS, cross_origin
from exposures import settings

from exposures.api.exposure.endpoints.exposure import ns as exposures_namespace

from exposures.api.restplus import api

app = Flask(__name__)
CORS(app)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


#def configure_app(flask_app):
#app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


#def initialize_app(flask_app):
#    configure_app(flask_app)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
#api.add_namespace(link_search_namespace)
app.register_blueprint(blueprint)
#db.init_app(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

def main():
    #initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()
