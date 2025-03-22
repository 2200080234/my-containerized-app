# Containerized Flask Application

This is a containerized Flask application with a complete CI/CD pipeline using Jenkins and infrastructure as code using Terraform.

## Project Structure

```
containerized-app/
│── app.py                 # Flask application
│── Dockerfile             # Docker configuration
│── requirements.txt       # Python dependencies
│── terraform/             # Terraform deployment scripts
│   ├── main.tf            # AWS infrastructure definition
│   ├── variables.tf       # Terraform variables
│   ├── outputs.tf         # Outputs for Terraform
│── jenkins/               # Jenkins CI/CD pipeline
│   ├── Jenkinsfile        # Jenkins pipeline configuration
│── README.md              # Documentation
```

## Prerequisites

- Python 3.9+
- Docker
- AWS CLI configured with appropriate credentials
- Terraform
- Jenkins server

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application locally:
```bash
python app.py
```

## Docker Build

To build the Docker image locally:

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## Infrastructure Deployment

1. Navigate to the terraform directory:
```bash
cd terraform
```

2. Initialize Terraform:
```bash
terraform init
```

3. Deploy the infrastructure:
```bash
terraform apply
```

Required variables:
- `vpc_id`: Your VPC ID
- `subnet_ids`: List of subnet IDs for ECS tasks

## CI/CD Pipeline

The Jenkins pipeline performs the following steps:
1. Checkout code
2. Build and test the application
3. Build Docker image
4. Push to Amazon ECR
5. Deploy to Amazon ECS

To set up the pipeline in Jenkins:
1. Create a new pipeline job
2. Configure the SCM to point to your repository
3. Set the pipeline script path to `jenkins/Jenkinsfile`
4. Configure AWS credentials in Jenkins

## AWS Resources Created

- ECR Repository for Docker images
- ECS Cluster and Service
- Security Groups
- IAM Roles and Policies
- CloudWatch Log Groups

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 