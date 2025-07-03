# 🚀 Technical Challenge – JSON API + Weekly Summary

This is my solution for the AWS technical assignment. It includes a simple API endpoint to accept JSON data, store it in DynamoDB, and (optionally) create a weekly summary that's saved to S3.

---

## 🛠️ What I Built

- A `POST /submit` API built with AWS Lambda + API Gateway (via AWS SAM).
- Data is stored in DynamoDB using ISO-formatted timestamps as IDs.
- Every week, a summary job runs via EventBridge, counts the total items, and stores a report to S3 in JSON format.

---

## 🔧 Tech & Tools Used

- **AWS SAM** – I chose SAM to keep things simple and deployable as a single stack.
- **DynamoDB** – for fast, serverless storage (using `PAY_PER_REQUEST` to stay in the Free Tier).
- **S3** – stores the weekly reports.
- **GitHub Actions** – used for CI/CD to deploy on every `main` push.

---

## 🤔 Why I Did It This Way

I focused on simplicity and practicality. I wanted to avoid overengineering but still demonstrate:
- An API that persists data
- Basic automation (with EventBridge)
- A clean, reproducible deployment

I also made some small changes to make it feel more real-world, like:
- Using a timestamp instead of UUID for easier sorting/debugging
- Separating logic into functions (`persist_data()` etc.)
- Writing clean, minimal YAML to avoid unnecessary SAM noise

---

## ✅ Conclusion

This challenge was fun to work on! I focused on keeping the code clean and understandable while following best practices (but not going overboard). Everything is deployable with the AWS Free Tier.

### 🤖 Disclaimer

This solution was developed with the help of official AWS documentation, online references, and AI-assisted tools, used primarily to validate ideas, troubleshoot, and speed up development. All decisions were still reviewed and applied with my own reasoning and intent.

---

## 🚀 How to Deploy

Make sure you have AWS SAM CLI installed:

```bash
sam build
sam deploy --guided

