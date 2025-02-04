# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MeasureParam(str, Enum):
    """
    MeasureParam
    """

    """
    allowed enum values
    """
    GEOMETRIC_MEAN = 'GEOMETRIC_MEAN'
    GEOMETRIC_LEAST_SQUARES_MEAN = 'GEOMETRIC_LEAST_SQUARES_MEAN'
    LEAST_SQUARES_MEAN = 'LEAST_SQUARES_MEAN'
    LOG_MEAN = 'LOG_MEAN'
    MEAN = 'MEAN'
    MEDIAN = 'MEDIAN'
    NUMBER = 'NUMBER'
    COUNT_OF_PARTICIPANTS = 'COUNT_OF_PARTICIPANTS'
    COUNT_OF_UNITS = 'COUNT_OF_UNITS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MeasureParam from a JSON string"""
        return cls(json.loads(json_str))


