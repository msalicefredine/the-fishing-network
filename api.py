# Define all roots

import falcon

from controller.root import HomePage
from controller.things import ThingsResource

app = falcon.API()

home = HomePage()

app.add_route('/home', home)

test = ThingsResource()

app.add_route('/things', test)