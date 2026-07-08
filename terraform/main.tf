terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "devops_dashboard" {
  name = "devops-dashboard:latest"
  build {
    context = "../"
  }
}

resource "docker_container" "devops_dashboard" {
  name  = "devops-dashboard"
  image = docker_image.devops_dashboard.image_id

  ports {
    internal = 5002
    external = 5002
  }

  env = [
    "GROQ_API_KEY=${var.groq_api_key}"
  ]
}

variable "groq_api_key" {
  description = "Groq API key"
  sensitive   = true
}