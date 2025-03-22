variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "flask-app"
}

variable "vpc_id" {
  description = "VPC ID where resources will be deployed"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for ECS tasks"
  type        = list(string)
}

variable "cpu" {
  description = "CPU units for the ECS task"
  type        = number
  default     = 256
}

variable "memory" {
  description = "Memory for the ECS task"
  type        = number
  default     = 512
}

variable "desired_count" {
  description = "Desired number of tasks running in the service"
  type        = number
  default     = 1
}

variable "key_name" {
  description = "Name of the SSH key pair to use for the EC2 instance"
  type        = string
} 