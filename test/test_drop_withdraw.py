# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clinicaltrials.models.drop_withdraw import DropWithdraw

class TestDropWithdraw(unittest.TestCase):
    """DropWithdraw unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DropWithdraw:
        """Test DropWithdraw
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DropWithdraw`
        """
        model = DropWithdraw()
        if include_optional:
            return DropWithdraw(
                type = '',
                comment = '',
                reasons = [
                    clinicaltrials.models.flow_stats.FlowStats(
                        group_id = '', 
                        comment = '', 
                        num_subjects = '', 
                        num_units = '', )
                    ]
            )
        else:
            return DropWithdraw(
        )
        """

    def testDropWithdraw(self):
        """Test DropWithdraw"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
