# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clinicaltrials.models.value_count import ValueCount

class TestValueCount(unittest.TestCase):
    """ValueCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValueCount:
        """Test ValueCount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValueCount`
        """
        model = ValueCount()
        if include_optional:
            return ValueCount(
                studies_count = 56,
                value = ''
            )
        else:
            return ValueCount(
                studies_count = 56,
                value = '',
        )
        """

    def testValueCount(self):
        """Test ValueCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
