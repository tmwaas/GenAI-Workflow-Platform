provider "azurerm" {
  features {}
  resource_provider_registrations = "none"  
}

# See the RG name by using this command: 'az group list --query "[].name" -o tsv'
data "azurerm_resource_group" "rg" {
  name = "1-da70a4dc-playground-sandbox" 
}

# Azure AI Search
resource "azurerm_search_service" "search" {
  name                = "search-banking-${random_string.suffix.result}"
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  sku                 = "basic"
}

# AKS Cluster 
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "aks-banking-${random_string.suffix.result}"
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name
  dns_prefix          = "bankaks"

  default_node_pool {
    name       = "system"
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}