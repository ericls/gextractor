import unittest
from gextractor.base import BaseExtractor
from gextractor.fields import PQField, Pq


class TestExtractor(BaseExtractor):
    title = PQField('title')
    heading = PQField('h1')
    body = PQField('p#body')
    heading_reverse = PQField('h1', callback=lambda x: x[::-1])


html = """
<!doctype html>
<html class="no-js" lang="">
    <head>
        <title>TITLE</title>
    </head>
    <body>
        <h1>Heading</h1>
        <p id="body">This is the body</p>
    </body>
</html>
"""


class TestBaseModel(unittest.TestCase):

    def test_with_url(self):
        pass

    def test_with_dom(self):
        extractor = TestExtractor(dom=Pq(html))
        self.assertEqual(extractor.body, "This is the body")
        self.assertEqual(extractor.title, "TITLE")
        self.assertEqual(extractor.heading, 'Heading')
        self.assertEqual(extractor.heading_reverse, 'Heading'[::-1])


if __name__ == '__main__':
    unittest.main()
