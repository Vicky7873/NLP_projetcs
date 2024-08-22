# NLP_projetcs

1. create env
conda create -n nlp python=3.12 -y
conda activate nlp

2. create a temp.py for project structure
3. Install all the required libs
4. Remeber the setup.py is to declare the textsummerizer folder as local package
5. Create the logger file and run the demo via main.py
6. Mentioned the few functions in the common.py
7. Hugging Face is a technology company known for its development of open-source tools and libraries that facilitate the creation and deployment of natural language processing (NLP) models. It has become one of the leading platforms in the field of artificial intelligence, particularly in NLP.

Key Components of Hugging Face:
Transformers Library:

Overview: The Hugging Face Transformers library is a popular Python library that provides pre-trained models for various NLP tasks like text classification, translation, summarization, and more. It supports models like BERT, GPT, T5, and many others.
Use Case: You can easily use these models for tasks like sentiment analysis, text generation, and question answering by leveraging the pre-trained models or fine-tuning them on your specific data.

# Remember these workflow steps will follow for all the steps like data ingestion/transformation/modeliing/evaluation etc.

# Workflows
1. Update config.yaml
here we will store the config things example data set path to get the data/store the data etc
2. Update params.yaml
3. Update entity
entity is nothing but the return type of a function
entity where we just store the data paths only, once configuration manager will execute then it will return the and store the data as per the entity data storage path
4. Update the configuration manager in src config
configuration manager where we will read the config/params yaml and and return the data to the entity folder, this will used in pipeline 
5. update the components
this .py file will zip unzip the data and store the data into the respective folder, once the configuration manager will execute then it will return the and store the data as per the entity data storage path
6. update the pipeline

7. update the main.py
to run the pipe line we need write the pieace of code
8. update the app.py

# why we need data validation?
A> bcoz some how if we got the in correct data/ wrongly formated data our model will through an error, so to avoid these things we should perform data validation

# 1. Login to AWS console.
# 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

# Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
# 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
# 7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app