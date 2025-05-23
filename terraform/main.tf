terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "my_fastapi_res" {
  name = "my_fastapi"
  build {
    path = ".."
    tag  = ["my_fastapi:develop"]
  }
}

resource "docker_container" "fastapi" {
  name  = "fastapi"
  image = docker_image.my_fastapi_res.image_id
  ports {
    internal = 8000
    external = 8002
  }
}
