resource "google_cloud_run_service" "chatbot" {
  name     = "chatbot"
  location = var.region

  template {
    spec {
      containers {
        image = var.image
      }
    }
  }

  traffics {
    percent         = 100
    latest_revision = true
  }
}
