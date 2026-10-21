#!/usr/bin/env bash

set -euo pipefail

# Pin the generator so regenerations are reproducible; bump deliberately.
GENERATOR_IMAGE="openapitools/openapi-generator-cli:v7.26.0"

# Package version tracks the API version in the spec.
API_VERSION=$(grep -E '^\s+version:' openapi-spec.yaml | head -1 | sed 's/.*version: "\(.*\)"/\1/')

if [ -z "$API_VERSION" ]; then
    echo "❌ Could not extract version from openapi-spec.yaml" >&2
    exit 1
fi

echo "Generating clinicaltrials $API_VERSION with $GENERATOR_IMAGE"

# disallowAdditionalPropertiesIfNotPresent=false: follow the OpenAPI/JSON Schema
# default (objects are open), so unknown fields from the API are kept in
# additional_properties instead of being silently dropped.
docker run --rm \
    -v "$(pwd):/local" \
    "$GENERATOR_IMAGE" \
    generate -i "/local/openapi-spec.yaml" -g python -o /local \
    --package-name clinicaltrials \
    --git-user-id everygene \
    --git-repo-id clinicaltrials-python \
    --additional-properties="packageVersion=${API_VERSION},packageUrl=https://github.com/everygene/clinicaltrials-python,buildSystem=hatchling,disallowAdditionalPropertiesIfNotPresent=false"
