import falcon
from mongoengine import connect
from dynaconf import settings as conf

from .api import Ping, TaskResource, BookResource


# connect to mongondb
connect(host=conf.get('MONGODB_HOST', '127.0.0.1'),
        port=conf.get('MONGODB_PORT', 27017))

# init falcon app
app = application = falcon.API()

# get ping resource
ping = Ping()

# get task resource
task = TaskResource()

# get books resource
books = BookResource()


# set route
app.add_route('/ping', ping)

# task route
app.add_route('/task/create', task)
app.add_route('/task/status/{task_id}', task)

# book route
app.add_route('/book/{book_id}', books)
app.add_route('/books/', books)

