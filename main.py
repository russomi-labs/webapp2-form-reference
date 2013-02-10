import os
import sys
import webapp2
import routes
import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

app = webapp2.WSGIApplication(debug=os.environ['SERVER_SOFTWARE'].startswith('Dev'), config=config.webapp2_config)
routes.add_routes(app)
