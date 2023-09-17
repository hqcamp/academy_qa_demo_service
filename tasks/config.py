import os

PACKAGE_VERSION = "0.0.0"
with open(os.path.join("./version"), mode="r") as version_file:
    PACKAGE_VERSION = version_file.readline()

SERVICE_NAME = "academy_qa_demo_service"
GENERATED_PATH = "./generated"

DOCKER_IMAGE_NAME = SERVICE_NAME
DOCKER_REGISTRY_PASSWORD = os.environ.get("DOCKERHUB_PASSWORD", "")
DOCKER_REGISTRY_USER = os.environ.get("DOCKERHUB_USERNAME", "")
DOCKER_IMAGE_REGISTRY = "docker.hub.com"
