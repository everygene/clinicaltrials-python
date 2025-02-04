# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clinicaltrials.models.baseline_measure import BaselineMeasure

class TestBaselineMeasure(unittest.TestCase):
    """BaselineMeasure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaselineMeasure:
        """Test BaselineMeasure
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaselineMeasure`
        """
        model = BaselineMeasure()
        if include_optional:
            return BaselineMeasure(
                title = '',
                description = '',
                population_description = '',
                param_type = 'GEOMETRIC_MEAN',
                dispersion_type = 'NA',
                unit_of_measure = '',
                calculate_pct = True,
                denom_units_selected = '',
                denoms = [
                    clinicaltrials.models.denom.Denom(
                        units = '', 
                        counts = [
                            clinicaltrials.models.denom_count.DenomCount(
                                group_id = '', 
                                value = '', )
                            ], )
                    ],
                classes = [
                    clinicaltrials.models.measure_class.MeasureClass(
                        title = '', 
                        denoms = [
                            clinicaltrials.models.denom.Denom(
                                units = '', 
                                counts = [
                                    clinicaltrials.models.denom_count.DenomCount(
                                        group_id = '', 
                                        value = '', )
                                    ], )
                            ], 
                        categories = [
                            clinicaltrials.models.measure_category.MeasureCategory(
                                title = '', 
                                measurements = [
                                    clinicaltrials.models.measurement.Measurement(
                                        group_id = '', 
                                        value = '', 
                                        spread = '', 
                                        lower_limit = '', 
                                        upper_limit = '', 
                                        comment = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return BaselineMeasure(
        )
        """

    def testBaselineMeasure(self):
        """Test BaselineMeasure"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
