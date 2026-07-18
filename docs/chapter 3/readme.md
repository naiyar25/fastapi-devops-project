# Chapter 3 - AWS IAM & AWS CLI Fundamentals (FloCI Implementation)

## Objective

The objective of this chapter is to understand AWS Identity and Access Management (IAM), configure the AWS CLI, and implement IAM resources using FloCI (AWS Emulator).

Although this project uses FloCI for local development, all concepts covered in this chapter are directly applicable to Amazon Web Services (AWS).

---

# Learning Outcomes

After completing this chapter, I can:

- Understand AWS Identity and Access Management (IAM)
- Create IAM Users
- Create IAM Groups
- Create Customer Managed Policies
- Attach Policies to Groups
- Understand the IAM permission model
- Configure and verify AWS CLI
- Understand AWS Regions and Availability Zones
- Learn IAM security best practices

---

# Project Environment

| Component | Value |
|-----------|-------|
| Platform | FloCI (AWS Emulator) |
| AWS CLI | Installed |
| Region | ap-south-1 |
| Output Format | JSON |

---

# IAM Architecture

```
                   IAM Policy
                        │
                        ▼
                 DevOps-Team Group
                        │
                        ▼
                naiyar-devops User
                        │
                        ▼
              AWS/FloCI Resources
```

The user inherits permissions through the IAM Group.

---

# IAM Resources Created

## IAM User

| Property | Value |
|----------|-------|
| User Name | naiyar-devops |
| Path | / |

Verification Command

```powershell
aws iam list-users
```

---

## IAM Group

| Property | Value |
|----------|-------|
| Group Name | DevOps-Team |

Verification Command

```powershell
aws iam list-groups
```

---

## Add User to Group

Command

```powershell
aws iam add-user-to-group --user-name naiyar-devops --group-name DevOps-Team
```

Verification

```powershell
aws iam get-group --group-name DevOps-Team
```

---

# Customer Managed Policy

Policy Name

```
S3ReadPolicy
```

Policy File

```
iam/s3-read-policy.json
```

Policy JSON

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3List",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": "*"
    }
  ]
}
```

Create Policy

```powershell
aws iam create-policy --policy-name S3ReadPolicy --policy-document file://iam/s3-read-policy.json
```

---

# Attach Policy to Group

Command

```powershell
aws iam attach-group-policy --group-name DevOps-Team --policy-arn arn:aws:iam::000000000000:policy/S3ReadPolicy
```

Verification

```powershell
aws iam list-attached-group-policies --group-name DevOps-Team
```

---

# AWS CLI Commands Used

## Verify Identity

```powershell
aws sts get-caller-identity
```

---

## List Users

```powershell
aws iam list-users
```

---

## List Groups

```powershell
aws iam list-groups
```

---

## Get Group Details

```powershell
aws iam get-group --group-name DevOps-Team
```

---

## List Policies

```powershell
aws iam list-policies
```

---

# IAM Permission Flow

```
Developer

↓

IAM User

↓

IAM Group

↓

IAM Policy

↓

AWS Resources
```

---

# AWS Concepts

## IAM User

Represents an individual identity.

Example

```
naiyar-devops
```

---

## IAM Group

A collection of IAM Users.

Example

```
DevOps-Team
```

Permissions should be assigned to Groups instead of individual Users.

---

## IAM Policy

A JSON document that defines permissions.

Types of IAM Policies:

- AWS Managed Policy
- Customer Managed Policy
- Inline Policy

---

## Authentication vs Authorization

Authentication

> Who are you?

Authorization

> What are you allowed to do?

---

# AWS Regions

A Region is a geographical location where AWS hosts data centers.

Examples

- ap-south-1
- us-east-1
- eu-west-1

This project uses:

```
ap-south-1
```

---

# Availability Zones

Each AWS Region contains multiple Availability Zones.

Example

- ap-south-1a
- ap-south-1b
- ap-south-1c

Availability Zones provide:

- High Availability
- Fault Tolerance
- Disaster Recovery

---

# IAM Security Best Practices

- Never use the Root User for daily work.
- Enable Multi-Factor Authentication (MFA).
- Follow the Principle of Least Privilege.
- Rotate Access Keys regularly.
- Use IAM Roles whenever possible.
- Store secrets securely.
- Remove unused IAM Users and Policies.
- Audit permissions periodically.

---

# Principle of Least Privilege

Grant only the minimum permissions required to perform a task.

❌ Bad Example

AdministratorAccess

✅ Good Example

Read-only access to a specific S3 bucket.

---

# Root Account Protection

The AWS Root Account should only be used for:

- Billing
- Account Recovery
- MFA Configuration

Daily administration should be performed using IAM Users.

---

# Exercises

1. Create a new IAM User.
2. Create a new IAM Group.
3. Add the user to the group.
4. Create a custom IAM Policy.
5. Attach the policy to the group.
6. Verify attached policies.
7. Explain the IAM permission flow.

---

# Interview Questions

1. What is IAM?
2. What is the difference between an IAM User and an IAM Role?
3. What is an IAM Group?
4. What is an IAM Policy?
5. Explain the structure of an IAM Policy.
6. What is the Principle of Least Privilege?
7. Why should the Root User not be used for daily work?
8. What is the difference between Authentication and Authorization?
9. What is an AWS Region?
10. What is an Availability Zone?
11. What are AWS Managed Policies?
12. What are Customer Managed Policies?
13. How do you verify AWS CLI credentials?
14. How do you attach a policy to a group?
15. Why are Groups preferred over assigning permissions directly to users?

---

# Chapter Summary

In this chapter, I successfully implemented IAM using FloCI and AWS CLI. I created an IAM User, IAM Group, Customer Managed Policy, attached the policy to the group, and verified the complete permission model.

This chapter also covered AWS Regions, Availability Zones, IAM security best practices, and the Principle of Least Privilege, providing a strong foundation for Infrastructure as Code and cloud security.

---

# Next Chapter

**Chapter 4 - Refactoring the FastAPI Application**

Topics include:

- Project Structure
- Logging
- Environment Variables
- Health Check Endpoint
- Metrics Endpoint
- Configuration Management
- Exception Handling
- Unit Testing
- Preparing the application for Docker