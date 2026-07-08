# Terraform

Deploys devops-dashboard as a Docker container via Terraform.

## Usage

```bash
cd terraform
terraform init
terraform apply -var="groq_api_key=your_key"
```