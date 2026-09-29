# Root teaching stack — composes multicloud modules (no backend — local state only if init ever run)
module "aws_landing" {
  source      = "../../modules/aws"
  environment = "teaching"
}

module "gcp_landing" {
  source     = "../../modules/gcp"
  project_id = "faiz-elahi-teaching-lab"
}

module "azure_landing" {
  source      = "../../modules/azure"
  environment = "teaching"
}

output "aws_vpc_id" {
  value = module.aws_landing.vpc_id
}

output "gcp_network" {
  value = module.gcp_landing.network_name
}

output "azure_rg" {
  value = module.azure_landing.resource_group_name
}
