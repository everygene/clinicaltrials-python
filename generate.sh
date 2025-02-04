#!/usr/bin/env bash

docker run --rm \
    -v "$(pwd):/local" \
    openapitools/openapi-generator-cli \
    generate -i "/local/openapi-spec.yaml" -g python -o /local --package-name clinicaltrials
