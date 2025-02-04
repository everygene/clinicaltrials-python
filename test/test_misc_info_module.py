# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clinicaltrials.models.misc_info_module import MiscInfoModule

class TestMiscInfoModule(unittest.TestCase):
    """MiscInfoModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MiscInfoModule:
        """Test MiscInfoModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MiscInfoModule`
        """
        model = MiscInfoModule()
        if include_optional:
            return MiscInfoModule(
                version_holder = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                removed_countries = [
                    ''
                    ],
                submission_tracking = clinicaltrials.models.submission_tracking.SubmissionTracking(
                    estimated_results_first_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    first_mcp_info = clinicaltrials.models.first_mcp_info.FirstMcpInfo(
                        post_date_struct = clinicaltrials.models.date_struct.DateStruct(
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            type = 'ACTUAL', ), ), 
                    submission_infos = [
                        clinicaltrials.models.submission_info.SubmissionInfo(
                            release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            unrelease_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            unrelease_date_unknown = True, 
                            reset_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            mcp_release_n = 56, )
                        ], )
            )
        else:
            return MiscInfoModule(
        )
        """

    def testMiscInfoModule(self):
        """Test MiscInfoModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
