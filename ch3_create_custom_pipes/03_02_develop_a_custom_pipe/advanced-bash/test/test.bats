#!/usr/bin/env bats

setup() {
  DOCKER_IMAGE=${DOCKER_IMAGE:="test/example"}

  echo "Building image..."
  docker build -t ${DOCKER_IMAGE}:test .
}

@test "Dummy test" {
    run docker run \
        -e NAME="baz" \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        ${DOCKER_IMAGE}:test

    echo "Status: $status"
    echo "Output: $output"

    [ "$status" -eq 0 ]
}

