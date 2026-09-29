variable "env" { type = string }
locals {
  layers = ["raw", "curated", "analytics"]
  clouds = ["aws", "azure", "gcp"]
  buckets = { for pair in setproduct(local.clouds, local.layers) :
    "${pair[0]}-${pair[1]}-${var.env}" => { cloud = pair[0], layer = pair[1] } }
}
output "bucket_map" { value = local.buckets }
