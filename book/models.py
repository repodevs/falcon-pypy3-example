from mongoengine import StringField, IntField, Document


class Book(Document):
    name = StringField()
    isbn = IntField()
    author = StringField()


