# 🌦️ Python Weather App with Docker & Kubernetes (Minikube)

This project demonstrates how to build a weather app using Flask and OpenWeatherMap API, containerize it using Docker, push the image to Docker Hub, and deploy it on a local Kubernetes cluster using Minikube.

---

## 📁 Folder Structure
python-weather-application/ ├── app.py ├── Dockerfile ├── requirements.txt ├── .env ├── deployment.yaml └── service.yaml


---

## 🚀 Prerequisites

Make sure you have the following installed:

- Python 3.7+
- Docker
- Docker Hub account
- Minikube
- kubectl
- Git

---

## 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/rxm-gupta/python-weather-application.git
cd python-weather-application
```

## 🌐 Step 2: Get OpenWeatherMap API Key

-Sign up at OpenWeatherMap
-Copy your API key
-Create a .env file in the root directory:
```bash
WEATHER_API_KEY=your_openweather_api_key
```

## 🐍 Step 3: Install Python Dependencies 

```bash
pip install -r requirements.txt
```

## 🔍 Step 4: Test the App Locally

```bash
python app.py
```
Then open in your browser:
```bash
http://localhost:5000
```

## 🐳 Step 5: Create Dockerfile [we already have one]


## 🛠️ Step 6: Build & Run Docker Image
```bash
docker build -t your-dockerhub-username/python-weather-application .
docker run -p 5000:5000 your-dockerhub-username/python-weather-application
```

## ☁️ Step 7: Push Image to Docker Hub
```bash
docker login
docker push your-dockerhub-username/python-weather-application
```

## ☸️ Step 8: Start Minikube
```bash
minikube start
```

## ⚙️ Step 9: Create deployment.yaml [we already have one]

## 📡 Step 10: Create service.yaml [we already have one]

## 🔐 Step 11: secret.yaml + WSL Encoding Instructions
```bash
# 🔐 Kubernetes Secret for OpenWeatherMap API Key
# Follow these steps to create the secret.yaml file

# 👣 Step 1: Open WSL from Start Menu

# 👣 Step 2: Run this command in WSL terminal
# Replace the string inside quotes with your real API key
echo -n "your_openweather_api_key_here" | base64

# It will return something like:
# eW91csdbfsdxlfdsjbsdkdflcmU=

# 👣 Step 3: Create `secret.yaml` file with the below content
# Replace the encoded string in 'value:' with your result

apiVersion: v1
kind: Secret
metadata:
  name: weather-api-secret
type: Opaque
data:
  WEATHER_API_KEY: eW91cl9hcGlfa2V5X2hlcmU=  # 👈 Your base64 encoded key
```

## 📥 Step 12: Apply Kubernetes Files
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f secret.yaml
```

## 📋 Step 13: Verify Deployment & Service
```bash
kubectl get pods
kubectl get svc
```

## 🌐 Step 14: Access the App in Browser
```bash
minikube service weather-app-service --url
Copy the URL it shows (something like http://192.168.49.2:30038) and open in your browser.
```

## ⚖️ Step 15: Scale the App
To scale the deployment to 3 replicas:
```bash
kubectl scale deployment weather-app-deployment --replicas=3
kubectl get pods
```

## 🧹 Step 16: Clean Up
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
minikube stop
```



✍️ Author
rxm-gupta - GitHub
🎯 Happy Coding & DevOps 🚀
