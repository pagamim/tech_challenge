# JSON Data API with Weekly Summary

## 💡 Overview

This project sets up a simple REST API on AWS to store incoming JSON payloads in DynamoDB and optionally generate weekly summaries saved to S3.

## 🚀 Features

- **/submit** API to store JSON entries
- **DynamoDB** for data storage using on-demand billing
- **EventBridge + Lambda** to generate weekly summaries
- **S3** for storing JSON reports
- **CI/CD** using GitHub Actions and AWS SAM

## 🧠 Design Rationale

- **SAM (Serverless Application Model):** Simple syntax, works seamlessly with GitHub Actions and supports fast deployments.
- **DynamoDB PAY_PER_REQUEST:** Chosen to stay inside the free tier and scale without needing to estimate capacity.
- **ISO Timestamps as IDs:** Helps keep the records sortable while being readable. I considered UUIDs but chose timestamps for debugging clarity.
- **Environment Variables:** Used for flexibility across environments, e.g., table name or bucket.

## 🔄 CI/CD Flow

- On every push to `main`, the workflow:
  1. Sets up Python + SAM
  2. Validates the template
  3. Builds and deploys the stack to AWS

I used GitHub Actions for simplicity and because it's free, integrated, and suits smaller workflows like this.

## 📦 Deployment Instructions

Ensure you have the AWS SAM CLI installed locally:

```bash
sam build
sam deploy --guided

