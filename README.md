# This is a collaborative CICD project with Lina and Jay

## Overview

This project is a small cloud application built to practise modern DevOps and AWS deployment patterns.

The application is made up of:

- a **frontend Flask application** that will run in a container on **AWS Fargate**
- a **backend AWS Lambda function** that provides data to the frontend through **Amazon API Gateway**
- a **Jenkins pipeline** that will automate testing and deployment

The goal is to build a simple but realistic end-to-end CI/CD workflow using GitHub, Jenkins, Docker, Fargate, API Gateway, and Lambda.

---

## Project Goal

The main goal of this project is to:

- deploy a containerised frontend application to AWS Fargate
- connect the frontend to a serverless backend powered by AWS Lambda
- expose the Lambda through Amazon API Gateway
- automate the testing and deployment process using Jenkins

This project is designed to help us understand how container-based services and serverless services can work together in a single application.

---

## Architecture

The target architecture for this project is:

```text
Browser
   ↓
Frontend Flask app on AWS Fargate
   ↓
Amazon API Gateway
   ↓
AWS Lambda
```

## Project Brief Reference

This project is based on the Makers guidance here:

[Desired application and deployment process](https://journey.makers.tech/pages/desired-application-and-deployment-process)