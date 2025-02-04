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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from clinicaltrials.models.contact import Contact
from clinicaltrials.models.location import Location
from clinicaltrials.models.official import Official
from typing import Optional, Set
from typing_extensions import Self

class ContactsLocationsModule(BaseModel):
    """
    ContactsLocationsModule
    """ # noqa: E501
    central_contacts: Optional[List[Contact]] = Field(default=None, alias="centralContacts")
    overall_officials: Optional[List[Official]] = Field(default=None, alias="overallOfficials")
    locations: Optional[List[Location]] = None
    __properties: ClassVar[List[str]] = ["centralContacts", "overallOfficials", "locations"]

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
        """Create an instance of ContactsLocationsModule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in central_contacts (list)
        _items = []
        if self.central_contacts:
            for _item_central_contacts in self.central_contacts:
                if _item_central_contacts:
                    _items.append(_item_central_contacts.to_dict())
            _dict['centralContacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in overall_officials (list)
        _items = []
        if self.overall_officials:
            for _item_overall_officials in self.overall_officials:
                if _item_overall_officials:
                    _items.append(_item_overall_officials.to_dict())
            _dict['overallOfficials'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item_locations in self.locations:
                if _item_locations:
                    _items.append(_item_locations.to_dict())
            _dict['locations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactsLocationsModule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "centralContacts": [Contact.from_dict(_item) for _item in obj["centralContacts"]] if obj.get("centralContacts") is not None else None,
            "overallOfficials": [Official.from_dict(_item) for _item in obj["overallOfficials"]] if obj.get("overallOfficials") is not None else None,
            "locations": [Location.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None
        })
        return _obj


