import unittest

from pyagents.detectors import ThresholdDetector

class TestThresholdDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ThresholdDetector()
        self.peak = [1, 2, 1, 0, -1, 10, 3.5, 2, 2.5, 3]
        self.nopeak = [1000, 1001, 999.0, 998, 1002.0]


    def test_one(self):
        ONE = ThresholdDetector.ONE

        self.assertTrue(self.detector.detect(self.peak))

        self.assertTrue(self.detector.detect(self.peak, threshold = 5, criteria = ONE))
        self.assertFalse(self.detector.detect(self.peak, threshold = 15, criteria = ONE))
        
        self.assertFalse(self.detector.detect(self.nopeak, threshold = 1005))
        self.assertTrue(self.detector.detect(self.nopeak, threshold = 995))

    def test_all(self):
        ALL = ThresholdDetector.ALL

        self.assertTrue(self.detector.detect(self.nopeak, threshold = 900, criteria = ALL))
        self.assertFalse(self.detector.detect(self.nopeak, threshold = 1000, criteria = ALL))

        # Corner case: must be strictly greater than lowest value
        self.assertFalse(self.detector.detect(self.peak, threshold = -1, criteria = ALL))

        # Only one value is greater
        self.assertFalse(self.detector.detect(self.peak, threshold = 9, criteria = ALL))

    def test_average(self):
        AVERAGE = ThresholdDetector.AVERAGE

        self.assertTrue(self.detector.detect(self.peak, threshold = 1, criteria = AVERAGE))
        self.assertFalse(self.detector.detect(self.peak, threshold = 5, criteria = AVERAGE))

        self.assertTrue(self.detector.detect(self.nopeak, threshold = 999, criteria = AVERAGE))
        
        
        
