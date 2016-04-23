# Define all roots

import falcon

from controller.root import HomePage
from controller.things import ThingsResource
from controller.upload import UploadPage
from controller.visualization import VisualizationPage
from controller.operations import Operations

app = falcon.API()

# set up home route
home = HomePage()
app.add_route('/home', home)

test = ThingsResource()
app.add_route('/things', test)

upload = UploadPage()
app.add_route('/upload', upload)

visualization = VisualizationPage()
app.add_route('/visualization',visualization)

# establish getting and posting operations data routes
operations = Operations()
app.add_route('/operations', operations)
