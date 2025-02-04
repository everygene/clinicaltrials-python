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
from clinicaltrials.models.responsible_party import ResponsibleParty
from clinicaltrials.models.sponsor import Sponsor
from typing import Optional, Set
from typing_extensions import Self

class SponsorCollaboratorsModule(BaseModel):
    """
    SponsorCollaboratorsModule
    """ # noqa: E501
    responsible_party: Optional[ResponsibleParty] = Field(default=None, alias="responsibleParty")
    lead_sponsor: Optional[Sponsor] = Field(default=None, alias="leadSponsor")
    collaborators: Optional[List[Sponsor]] = None
    __properties: ClassVar[List[str]] = ["responsibleParty", "leadSponsor", "collaborators"]

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
        """Create an instance of SponsorCollaboratorsModule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of responsible_party
        if self.responsible_party:
            _dict['responsibleParty'] = self.responsible_party.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lead_sponsor
        if self.lead_sponsor:
            _dict['leadSponsor'] = self.lead_sponsor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in collaborators (list)
        _items = []
        if self.collaborators:
            for _item_collaborators in self.collaborators:
                if _item_collaborators:
                    _items.append(_item_collaborators.to_dict())
            _dict['collaborators'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SponsorCollaboratorsModule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "responsibleParty": ResponsibleParty.from_dict(obj["responsibleParty"]) if obj.get("responsibleParty") is not None else None,
            "leadSponsor": Sponsor.from_dict(obj["leadSponsor"]) if obj.get("leadSponsor") is not None else None,
            "collaborators": [Sponsor.from_dict(_item) for _item in obj["collaborators"]] if obj.get("collaborators") is not None else None
        })
        return _obj


