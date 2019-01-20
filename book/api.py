import falcon
import json

from celery.result import AsyncResult

from .models import Book

from .tasks import fib


class Ping(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps('pong!')


class TaskResource(object):

    def on_post(self, req, resp):
        raw_json = req.stream.read().decode('utf-8') # https://stackoverflow.com/a/47731139
        result = json.loads(raw_json, encoding='utf-8')
        task = fib.delay(int(result['number']))
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            }
        }
        resp.body = json.dumps(result)

    def on_get(self, req, resp, task_id):
        """ Get Task Status by ID
        """
        task_result = AsyncResult(task_id)
        result = {'status': task_result.status, 'result': task_result.result}
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result)


class BookResource(object):

    def on_get(self, req, resp, book_id):
        """
        :param req: A request object
        :param resp: A response object
        :param book_id: book_id receive in http path to query book object
        :return:
            """
        book_obj = Book.objects.get(id=book_id)
        resp.body = json.dumps({
            'author': book_obj.author,
            'name': book_obj.name,
            'isbn': book_obj.isbn
        })
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        """
        :param req: A request object
        :param resp: A response object
        :return:
        """
        # req.media will deserialize json object
        book_data = req.media
        book_obj = Book.objects.create(**book_data)
        resp.body = json.dumps({'book_id': str(book_obj.id), 'message': 'book successfully created'})
        resp.status = falcon.HTTP_200

