from __future__ import print_function
from base import BaseSpider
from fields import PQField, PQListField
from six import print_ as print


class PythonDocSpider(BaseSpider):

    title = PQField('h1', format='text')
    content = PQField('p')
    functions = PQListField('dl.function', format='element')


b = PythonDocSpider(
    'https://docs.python.org/3/library/base64.html#module-base64'
)
print(b.title, b.content)
