# Define all roots

import falcon

from controller.root import HomePage
from controller.things import ThingsResource
from controller.upload import UploadPage
from controller.visualization import VisualizationPage
from controller.operations import Operations
from controller.catches import Catches
from controller.species import Species
from controller.view_datasets import ViewDatasetsPage
from controller.homeDataset import HomeDataset
from controller.verify import VerifyPage

app = falcon.API()

# set up home route
home = HomePage()
app.add_route('/home', home)
app.add_route('/', home)

test = ThingsResource()
app.add_route('/things', test)

upload = UploadPage()
app.add_route('/upload', upload)

verify = VerifyPage(upload)
app.add_route('/verify/{filename}', verify)

visualization = VisualizationPage()
app.add_route('/visualization',visualization)

view_datasets = ViewDatasetsPage()
app.add_route('/viewdatasets', view_datasets)

# establish getting and posting operations data routes
operations = Operations()
app.add_route('/operations', operations)

#establish get and post route for catch data
catches = Catches()
app.add_route('/catches', catches)

# establish get/post routes for species data
species = Species()
app.add_route('/species', species)

homeData = HomeDataset()
app.add_route('/homeData', homeData)