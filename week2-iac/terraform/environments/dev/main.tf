terraform {
  backend "s3" {
    bucket = "prep-tf-state-sunilvajja"
    key = "dev/network/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "prep-tf-lock"
    encrypt = true
  }
}

provider "aws" {
    region = "us-east-1"
}

module "network" {
    source = "../../modules/network"
    vpc_cidr = "10.0.0.0/16"
    subnet_cidr = "10.0.1.0/24"
    availability_zone = "us-east-1a"
    name_prefix = "prep-dev"
}

output "vpc_id" {
    value = module.network.vpc_id
}

output "subnet_id" {
    value = module.network.subnet_id
}
