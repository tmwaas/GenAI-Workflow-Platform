resource "azurerm_search_service" "genai" {
  name                = "genai-search-${var.env}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "standard"
}

resource "azurerm_search_index" "vector_index" {
  name                = "documents-vector-index"
  search_service_name = azurerm_search_service.genai.name
  resource_group_name = azurerm_resource_group.rg.name

  field {
    name = "id"
    type = "Edm.String"
    key  = true
  }

  field {
    name = "content"
    type = "Edm.String"
  }

  field {
    name = "contentVector"
    type = "Collection(Edm.Single)"
    searchable = true
    vector_search_dimensions = 1536
    vector_search_profile     = "default"
  }
}
