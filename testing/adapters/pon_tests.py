import unittest
import os

from pyagents.adapters import PointOfNeedDiagnosticAdapter


class TestPointOfNeedDiagnosticAdaptor(unittest.TestCase):

    def setUp(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        self.data_path = os.path.join(cur_path, 'data')

    def test_benice(self):
        xml_name = os.path.join(self.data_path, 'benice.xml')
        json_name = os.path.join(self.data_path, 'benice.json')
        with open(xml_name, 'r') as cur_xml:
            contents = cur_xml.read()
            adapter = PointOfNeedDiagnosticAdapter()
            output = adapter.adapt(contents)
        with open(json_name, 'r') as cur_json:
            self.assertEqual(output, cur_json.read())

    def test_operator(self):
        xml_name = os.path.join(self.data_path, 'test_operator.xml')
        json_name = os.path.join(self.data_path, 'test_operator.json')
        with open(xml_name, 'r') as cur_xml:
            contents = cur_xml.read()
            adapter = PointOfNeedDiagnosticAdapter()
            output = adapter.adapt(contents)
        with open(json_name, 'r') as cur_json:
            self.assertEqual(output, cur_json.read())

if __name__ == '__main__':
    unittest.main()
