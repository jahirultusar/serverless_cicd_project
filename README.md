# This is a collaborative CICD project with Lina and Jay

Project setup (first step):
- Pull the github repo to local
then go to you cloned repo directory root and run:
    - docker build -t serverless_cicd_practice .
Once image is built in your local then run 
    - docker run -d -p 5000:5000 serverless_cicd_practice

