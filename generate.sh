#!/usr/bin/env bash

set -euo pipefail

# Run OpenAPI generator
docker run --rm \
    -v "$(pwd):/local" \
    openapitools/openapi-generator-cli \
    generate -i "/local/openapi-spec.yaml" -g python -o /local --package-name clinicaltrials

# Extract API version from spec and update pyproject.toml
API_VERSION=$(grep -E '^\s+version:' openapi-spec.yaml | head -1 | sed 's/.*version: "\(.*\)"/\1/')

if [ -n "$API_VERSION" ]; then
    echo "Syncing package version to API version: $API_VERSION"
    sed -i "s/^version = .*/version = \"$API_VERSION\"/" pyproject.toml
    echo "✅ Package version updated to $API_VERSION"
else
    echo "⚠️  Warning: Could not extract version from openapi-spec.yaml"
fi
