terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.45"
    }
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

resource "hcloud_server" "devops" {
  name        = "devops-dashboard"
  image       = "ubuntu-24.04"
  server_type = "cx22"
  location    = "nbg1"

  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y docker.io docker-compose-plugin
    systemctl enable docker
    systemctl start docker
  EOF
}

variable "hcloud_token" {
  description = "Hetzner Cloud API token"
  sensitive   = true
}

output "server_ip" {
  value = hcloud_server.devops.ipv4_address
}