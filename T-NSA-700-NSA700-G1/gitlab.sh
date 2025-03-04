#!/bin/sh
# Get the registration token from:
# http://localhost/root/${project}/settings/ci_cd

registration_token="KrscBuZyDCKxDrbEC1yg"

docker exec -it gitlab-runner1 \
    gitlab-runner register \
    --non-interactive \
    --registration-token ${registration_token} \
    --locked=false \
    --description docker-stable \
    --url http://gitlab-web \
    --executor docker \
    --docker-image docker:stable \
    --docker-volumes "/var/run/docker.sock:/var/run/docker.sock" \
    --docker-network-mode gitlab-network