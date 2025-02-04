# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clinicaltrials.models.references_module import ReferencesModule

class TestReferencesModule(unittest.TestCase):
    """ReferencesModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferencesModule:
        """Test ReferencesModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferencesModule`
        """
        model = ReferencesModule()
        if include_optional:
            return ReferencesModule(
                references = [
                    clinicaltrials.models.reference.Reference(
                        pmid = '', 
                        type = 'BACKGROUND', 
                        citation = '', 
                        retractions = [
                            clinicaltrials.models.retraction.Retraction(
                                pmid = '', 
                                source = '', )
                            ], )
                    ],
                see_also_links = [
                    clinicaltrials.models.see_also_link.SeeAlsoLink(
                        label = '', 
                        url = '', )
                    ],
                avail_ipds = [
                    clinicaltrials.models.avail_ipd.AvailIpd(
                        id = '', 
                        type = '', 
                        url = '', 
                        comment = '', )
                    ]
            )
        else:
            return ReferencesModule(
        )
        """

    def testReferencesModule(self):
        """Test ReferencesModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
