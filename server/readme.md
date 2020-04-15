# Please Remember How::
1. Create a new Firebase project, or use an existing one.

 - Click Database and Create database in the Cloud Firestore section.
 - Set your security rules and location.

2. Download your Firebase Service Account Key.
 -  Click the Settings icon at the top of the dashboard.
 -  Click the Service Account tab.
 -  Select Python option for Admin SDK configuration snippet, click Generate new private key, and save it as key.json. ---- (find out later where to put this)

3. Create a new GCP project, or use an existing one. You need the project so that you can deploy to Cloud Run.

4. Open Cloud Shell or install the SDK
5. (Optional) To set up continuous deplyment follw the instructions [here](https://fullstackgcp.com/simplified-continuous-deployment-on-google-cloud-platform-bc5b0a025c4e)


### add to the top of the app.py

>import os  
>import uuid  
>import stripe  
>import firebase_admin  

>from firebase_admin import credentials  
>from flask import Flask, jsonify, request  
>from flask_cors import CORS  


### create a dockerfile in the server directory

>FROM python:3.7-stretch  
>RUN apt-get update -y  
>RUN apt-get install -y python-pip python-dev build-essential  
>COPY . /app  
>WORKDIR /app  
>RUN pip install -r requirements.txt  
>EXPOSE 5000/tcp  
>ENTRYPOINT ["python"]  
>CMD ["app.py"]  

### create cloudbuild.yaml
Look at this as a yaml file... until I figure out how to make the markdown not butcher this

boner-boiz is the id of the project that we are using, this can be found by going into the Cloud Run console and using the dropdown at the top to choose the project that is desired, and then referencing the id



>steps:  
>  # build & push the container image  
>\- name: "gcr.io/kaniko-project/executor:latest"  
>   args: ["--cache=true", "--cache-ttl=48h", "--destination=gcr.io/boner-boiz/games-api:latest"]  
>  # Deploy container image to Cloud Run  
>\- name: "gcr.io/cloud-builders/gcloud"  
>   args: ['beta', 'run', 'deploy', 'todo', '--image', 'gcr.io/boner-boiz/games-api:latest', '--region', 'us-central1', '--allow-unauthenticated', '--platform', 'managed']  

	### insert at the bottom of the app.py - just below the if __name__ == '__main__':
>	app.run(host='0.0.0.0')  

requirements.txt

>	Flask==1.0.2  
>	Flask-Cors==3.0.7  
>	firebase_admin  
>	stripe  




### build docker container and then run it on successful build for testing
>docker build -t games-api  
>docker run games-api  

### gcloud container build 
**NOTE** may need to enable billing on the project/service -- Blaze pay-as-you-go  
>gcloud builds submit --config cloudbuild.yaml .  
Then when that has worked:  
Go to your Cloud Run   
create service  
select project  
choose platform (fully managed for us)  
choose a service name (games-api for us)  
allow unauthenticated  
next  
???

### 