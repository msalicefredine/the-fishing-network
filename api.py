# Define all roots

import falcon

from controller.root import HomePage
from controller.things import ThingsResource
from controller.upload import UploadPage
from controller.visualization import VisualizationPage

app = falcon.API()

home = HomePage()

app.add_route('/home', home)

test = ThingsResource()

app.add_route('/things', test)

upload = UploadPage()

app.add_route('/upload', upload)

visualization = VisualizationPage()

app.add_route('/visualization',visualization)
