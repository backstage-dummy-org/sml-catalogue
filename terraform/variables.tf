variable "environment" {
  type = string
}

locals {
  domain_name_base = {
    dev : "dev-sml.aws.onsdigital.uk."
    preprod : "preprod-sml.aws.onsdigital.uk."
    prod : "prod-sml.aws.onsdigital.uk."
  }
}
