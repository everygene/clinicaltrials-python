# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from clinicaltrials.models.event_assessment import EventAssessment
from clinicaltrials.models.event_stats import EventStats
from typing import Optional, Set
from typing_extensions import Self

class AdverseEvent(BaseModel):
    """
    AdverseEvent
    """ # noqa: E501
    term: Optional[StrictStr] = None
    organ_system: Optional[StrictStr] = Field(default=None, alias="organSystem")
    source_vocabulary: Optional[StrictStr] = Field(default=None, alias="sourceVocabulary")
    assessment_type: Optional[EventAssessment] = Field(default=None, alias="assessmentType")
    notes: Optional[StrictStr] = None
    stats: Optional[List[EventStats]] = None
    __properties: ClassVar[List[str]] = ["term", "organSystem", "sourceVocabulary", "assessmentType", "notes", "stats"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AdverseEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item_stats in self.stats:
                if _item_stats:
                    _items.append(_item_stats.to_dict())
            _dict['stats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdverseEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "term": obj.get("term"),
            "organSystem": obj.get("organSystem"),
            "sourceVocabulary": obj.get("sourceVocabulary"),
            "assessmentType": obj.get("assessmentType"),
            "notes": obj.get("notes"),
            "stats": [EventStats.from_dict(_item) for _item in obj["stats"]] if obj.get("stats") is not None else None
        })
        return _obj


