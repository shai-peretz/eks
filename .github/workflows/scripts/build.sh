#!/bin/bash

major_minor_patch="${MAJOR_MINOR_PATCH}"
tag_latest="${TAG_LATEST}"
docker_repo_name="${DOCKER_REPO_NAME}"
docker_image_name="${DOCKER_IMAGE_NAME}"

dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
source "${dir_path}/../common.sh"

bump_docker_image_version "${docker_repo_name}" "${docker_image_name}" "${major_minor_patch}"

#echo "${new_version}"

docker build --no-cache -t "${docker_repo_name}/${docker_image_name}:${new_version}" \
  --build-arg PORT=5000 .

docker_login "${DOCKERHUB_USERNAME}" "${DOCKERHUB_PASSWORD}" || die 'unable to login to docker hub' >/dev/null 2>&1

docker push docker.io/"${docker_repo_name}/${docker_image_name}:${new_version}"

tag_latest=$(upper_to_lower "${tag_latest}")

if [[ "${tag_latest}" =~ (true|"true") ]]; then
  docker tag "${docker_repo_name}/${docker_image_name}:${new_version}" "${docker_repo_name}/${docker_image_name}:latest"
  docker push "${docker_repo_name}/${docker_image_name}:latest"
fi

bump_docker_image_version {
  echo "asd"
}