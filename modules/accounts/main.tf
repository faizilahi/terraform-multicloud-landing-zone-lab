variable "org_name" { type = string default = "synth-data-org" }
locals {
  accounts = {
    data_dev  = { id = "000000000001", name = "data-dev" }
    data_prod = { id = "000000000002", name = "data-prod" }
  }
}
output "account_ids" { value = local.accounts }
