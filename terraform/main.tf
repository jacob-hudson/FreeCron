// Configure the Google Cloud provider
provider "google" {
 credentials = "${file("~/.gcp/creds.json")}"
 project     = "${var.project_name}"
 region      = "us-central1"
}

// remote backend on Google Cloud Storage
terraform {
  backend "gcs" {
  }
}

resource "google_pubsub_topic" "example" {
  name = "tf-test-topic"
}

resource "google_app_engine_application" "app" {
  project     = "${var.project_name}"
  location_id = "us-central"
}