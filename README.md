# clinicaltrials
This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.3
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clinicaltrials
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clinicaltrials
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import clinicaltrials
from clinicaltrials.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = clinicaltrials.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)



# Enter a context with an instance of the API client
with clinicaltrials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clinicaltrials.StatsApi(api_client)
    types = [] # List[FieldStatsType] | Filter by field types (optional) (default to [])
    fields = ['[\"Phase\"]'] # List[str] | Filter by piece names or field paths of leaf fields. See [Data Structure](/data-api/about-api/study-data-structure) for the available values.  If specified, must be non-empty comma- or pipe-separated list of fields to return. (optional)

    try:
        # Field Values
        api_response = api_instance.field_values_stats(types=types, fields=fields)
        print("The response of StatsApi->field_values_stats:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->field_values_stats: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://clinicaltrials.gov/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StatsApi* | [**field_values_stats**](docs/StatsApi.md#field_values_stats) | **GET** /stats/field/values | Field Values
*StatsApi* | [**list_field_sizes_stats**](docs/StatsApi.md#list_field_sizes_stats) | **GET** /stats/field/sizes | List Field Sizes
*StatsApi* | [**size_stats**](docs/StatsApi.md#size_stats) | **GET** /stats/size | Study Sizes
*StudiesApi* | [**enums**](docs/StudiesApi.md#enums) | **GET** /studies/enums | Enums
*StudiesApi* | [**fetch_study**](docs/StudiesApi.md#fetch_study) | **GET** /studies/{nctId} | Single Study
*StudiesApi* | [**list_studies**](docs/StudiesApi.md#list_studies) | **GET** /studies | Studies
*StudiesApi* | [**search_areas**](docs/StudiesApi.md#search_areas) | **GET** /studies/search-areas | Search Areas
*StudiesApi* | [**studies_metadata**](docs/StudiesApi.md#studies_metadata) | **GET** /studies/metadata | Data Model Fields
*VersionApi* | [**version**](docs/VersionApi.md#version) | **GET** /version | Version


## Documentation For Models

 - [AdverseEvent](docs/AdverseEvent.md)
 - [AdverseEventsModule](docs/AdverseEventsModule.md)
 - [AgencyClass](docs/AgencyClass.md)
 - [AgreementRestrictionType](docs/AgreementRestrictionType.md)
 - [AnalysisDispersionType](docs/AnalysisDispersionType.md)
 - [AnnotationModule](docs/AnnotationModule.md)
 - [AnnotationSection](docs/AnnotationSection.md)
 - [ArmGroup](docs/ArmGroup.md)
 - [ArmGroupType](docs/ArmGroupType.md)
 - [ArmsInterventionsModule](docs/ArmsInterventionsModule.md)
 - [AvailIpd](docs/AvailIpd.md)
 - [BaselineCharacteristicsModule](docs/BaselineCharacteristicsModule.md)
 - [BaselineMeasure](docs/BaselineMeasure.md)
 - [BioSpec](docs/BioSpec.md)
 - [BioSpecRetention](docs/BioSpecRetention.md)
 - [BooleanStats](docs/BooleanStats.md)
 - [BrowseBranch](docs/BrowseBranch.md)
 - [BrowseLeaf](docs/BrowseLeaf.md)
 - [BrowseLeafRelevance](docs/BrowseLeafRelevance.md)
 - [BrowseModule](docs/BrowseModule.md)
 - [CertainAgreement](docs/CertainAgreement.md)
 - [ConditionsModule](docs/ConditionsModule.md)
 - [ConfidenceIntervalNumSides](docs/ConfidenceIntervalNumSides.md)
 - [Contact](docs/Contact.md)
 - [ContactRole](docs/ContactRole.md)
 - [ContactsLocationsModule](docs/ContactsLocationsModule.md)
 - [DateStats](docs/DateStats.md)
 - [DateStruct](docs/DateStruct.md)
 - [DateType](docs/DateType.md)
 - [Denom](docs/Denom.md)
 - [DenomCount](docs/DenomCount.md)
 - [DerivedSection](docs/DerivedSection.md)
 - [DescriptionModule](docs/DescriptionModule.md)
 - [DesignAllocation](docs/DesignAllocation.md)
 - [DesignInfo](docs/DesignInfo.md)
 - [DesignMasking](docs/DesignMasking.md)
 - [DesignModule](docs/DesignModule.md)
 - [DesignTimePerspective](docs/DesignTimePerspective.md)
 - [DistItem](docs/DistItem.md)
 - [DocumentSection](docs/DocumentSection.md)
 - [DropWithdraw](docs/DropWithdraw.md)
 - [EligibilityModule](docs/EligibilityModule.md)
 - [EnrollmentInfo](docs/EnrollmentInfo.md)
 - [EnrollmentType](docs/EnrollmentType.md)
 - [EnumInfo](docs/EnumInfo.md)
 - [EnumItem](docs/EnumItem.md)
 - [EnumStats](docs/EnumStats.md)
 - [EventAssessment](docs/EventAssessment.md)
 - [EventGroup](docs/EventGroup.md)
 - [EventStats](docs/EventStats.md)
 - [ExpandedAccessInfo](docs/ExpandedAccessInfo.md)
 - [ExpandedAccessStatus](docs/ExpandedAccessStatus.md)
 - [ExpandedAccessTypes](docs/ExpandedAccessTypes.md)
 - [FieldNode](docs/FieldNode.md)
 - [FieldStatsType](docs/FieldStatsType.md)
 - [FieldValuesStats](docs/FieldValuesStats.md)
 - [FirstMcpInfo](docs/FirstMcpInfo.md)
 - [FlowGroup](docs/FlowGroup.md)
 - [FlowMilestone](docs/FlowMilestone.md)
 - [FlowPeriod](docs/FlowPeriod.md)
 - [FlowStats](docs/FlowStats.md)
 - [GeoPoint](docs/GeoPoint.md)
 - [GzipStats](docs/GzipStats.md)
 - [IdentificationModule](docs/IdentificationModule.md)
 - [IntegerStats](docs/IntegerStats.md)
 - [Intervention](docs/Intervention.md)
 - [InterventionType](docs/InterventionType.md)
 - [InterventionalAssignment](docs/InterventionalAssignment.md)
 - [IpdSharing](docs/IpdSharing.md)
 - [IpdSharingInfoType](docs/IpdSharingInfoType.md)
 - [IpdSharingStatementModule](docs/IpdSharingStatementModule.md)
 - [LargeDoc](docs/LargeDoc.md)
 - [LargeDocumentModule](docs/LargeDocumentModule.md)
 - [LimitationsAndCaveats](docs/LimitationsAndCaveats.md)
 - [ListSize](docs/ListSize.md)
 - [ListSizes](docs/ListSizes.md)
 - [Location](docs/Location.md)
 - [LongestString](docs/LongestString.md)
 - [MaskingBlock](docs/MaskingBlock.md)
 - [MeasureAnalysis](docs/MeasureAnalysis.md)
 - [MeasureCategory](docs/MeasureCategory.md)
 - [MeasureClass](docs/MeasureClass.md)
 - [MeasureDispersionType](docs/MeasureDispersionType.md)
 - [MeasureGroup](docs/MeasureGroup.md)
 - [MeasureParam](docs/MeasureParam.md)
 - [Measurement](docs/Measurement.md)
 - [Mesh](docs/Mesh.md)
 - [MiscInfoModule](docs/MiscInfoModule.md)
 - [MoreInfoModule](docs/MoreInfoModule.md)
 - [NonInferiorityType](docs/NonInferiorityType.md)
 - [NumberStats](docs/NumberStats.md)
 - [ObservationalModel](docs/ObservationalModel.md)
 - [Official](docs/Official.md)
 - [OfficialRole](docs/OfficialRole.md)
 - [OrgStudyIdInfo](docs/OrgStudyIdInfo.md)
 - [OrgStudyIdType](docs/OrgStudyIdType.md)
 - [Organization](docs/Organization.md)
 - [Outcome](docs/Outcome.md)
 - [OutcomeMeasure](docs/OutcomeMeasure.md)
 - [OutcomeMeasureType](docs/OutcomeMeasureType.md)
 - [OutcomeMeasuresModule](docs/OutcomeMeasuresModule.md)
 - [OutcomesModule](docs/OutcomesModule.md)
 - [OversightModule](docs/OversightModule.md)
 - [PagedStudies](docs/PagedStudies.md)
 - [PartialDateStruct](docs/PartialDateStruct.md)
 - [ParticipantFlowModule](docs/ParticipantFlowModule.md)
 - [Phase](docs/Phase.md)
 - [PointOfContact](docs/PointOfContact.md)
 - [PrimaryPurpose](docs/PrimaryPurpose.md)
 - [ProtocolSection](docs/ProtocolSection.md)
 - [RecruitmentStatus](docs/RecruitmentStatus.md)
 - [Reference](docs/Reference.md)
 - [ReferenceType](docs/ReferenceType.md)
 - [ReferencesModule](docs/ReferencesModule.md)
 - [ReportingStatus](docs/ReportingStatus.md)
 - [ResponsibleParty](docs/ResponsibleParty.md)
 - [ResponsiblePartyType](docs/ResponsiblePartyType.md)
 - [ResultsSection](docs/ResultsSection.md)
 - [Retraction](docs/Retraction.md)
 - [SamplingMethod](docs/SamplingMethod.md)
 - [SearchArea](docs/SearchArea.md)
 - [SearchDocument](docs/SearchDocument.md)
 - [SearchPart](docs/SearchPart.md)
 - [SecondaryIdInfo](docs/SecondaryIdInfo.md)
 - [SecondaryIdType](docs/SecondaryIdType.md)
 - [SeeAlsoLink](docs/SeeAlsoLink.md)
 - [Sex](docs/Sex.md)
 - [Sponsor](docs/Sponsor.md)
 - [SponsorCollaboratorsModule](docs/SponsorCollaboratorsModule.md)
 - [StandardAge](docs/StandardAge.md)
 - [Status](docs/Status.md)
 - [StatusModule](docs/StatusModule.md)
 - [StringStats](docs/StringStats.md)
 - [Study](docs/Study.md)
 - [StudySize](docs/StudySize.md)
 - [StudyType](docs/StudyType.md)
 - [SubmissionInfo](docs/SubmissionInfo.md)
 - [SubmissionTracking](docs/SubmissionTracking.md)
 - [UnpostedAnnotation](docs/UnpostedAnnotation.md)
 - [UnpostedEvent](docs/UnpostedEvent.md)
 - [UnpostedEventType](docs/UnpostedEventType.md)
 - [ValueCount](docs/ValueCount.md)
 - [Version](docs/Version.md)
 - [ViolationAnnotation](docs/ViolationAnnotation.md)
 - [ViolationEvent](docs/ViolationEvent.md)
 - [ViolationEventType](docs/ViolationEventType.md)
 - [WebLink](docs/WebLink.md)
 - [WhoMasked](docs/WhoMasked.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




