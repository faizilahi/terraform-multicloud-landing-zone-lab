terraform {
  required_version = ">= 1.5.0"
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "environment" {
  type    = string
  default = "lab"
}

resource "azurerm_resource_group" "landing" {
  name     = "rg-landing-${var.environment}"
  location = var.location
  tags = {
    Purpose = "Educational skeleton — do not apply to production subscription"
  }
}

resource "azurerm_storage_account" "landing" {
  name                     = "stlanding${var.environment}lab"
  resource_group_name      = azurerm_resource_group.landing.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

output "resource_group_name" {
  value = azurerm_resource_group.landing.name
}
