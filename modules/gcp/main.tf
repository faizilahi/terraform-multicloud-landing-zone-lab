terraform {
  required_version = ">= 1.5.0"
}

variable "project_id" {
  type        = string
  description = "Teaching placeholder — not a real project"
  default     = "example-lab-project"
}

variable "region" {
  type    = string
  default = "us-central1"
}

resource "google_compute_network" "landing" {
  name                    = "landing-vpc-lab"
  auto_create_subnetworks = false
  project                 = var.project_id
}

resource "google_storage_bucket" "landing_logs" {
  name     = "${var.project_id}-landing-logs-lab-teaching"
  location = var.region
  project  = var.project_id
}

output "network_name" {
  value = google_compute_network.landing.name
}
