# MVS Tool – Installation Guide

This guide provides detailed instructions on how to set up and run the Migration and Validation Suite (MVS Tool) locally, containerize it with Docker, and deploy it on a remote desktop for client access.

---

## 1. Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/your-username/mvs-tool.git
cd mvs-tool
```

---

## 2. Run Locally (Without Docker)

### Prerequisites

- Python 3.9 or higher  
- pip (Python package manager)  
- virtualenv (optional but recommended)

### Steps

Create and activate a virtual environment:

**On Unix/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Once running, the application will be accessible at:

```
http://localhost:8080
```

---

## 3. Run Using Docker (Local Development)

### Prerequisites

- Docker installed on your system

### Build the Docker image

```bash
docker build -t mvs-tool .
```

### Run the Docker container

```bash
docker run -d -p 8080:8080 --name mvs-container mvs-tool
```

The tool will now be accessible at:

```
http://localhost:8080
```

---

## 4. Run on Client Remote Desktop (Using Docker Image)

The client can run the MVS Tool on their remote desktop by installing Docker and pulling the image.

### Steps

1. **Install Docker Desktop** (Windows/macOS) or Docker Engine (Linux).

   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. **Pull the Docker image from the registry** (e.g., Docker Hub):

   ```bash
   docker pull your-dockerhub-username/mvs-tool:latest
   ```

   Replace `your-dockerhub-username/mvs-tool` with the actual image path you’ve pushed.

3. **Run the Docker container**:

   ```bash
   docker run -d -p 5000:5000 --name mvs-container your-dockerhub-username/mvs-tool:latest
   ```

4. **Access the application** on the remote desktop browser:

   ```
   http://localhost:8080
   ```

### Firewall Note

Ensure port `8080` is open on the remote desktop’s firewall if accessed externally.

## 5. Notes

- All required Python packages are defined in `requirements.txt`.
- Use `-v` to persist uploads or logs via Docker volumes or mounts.
- For production deployments, consider using Nginx as a reverse proxy with HTTPS.
- Common Docker commands:

```bash
# View logs
docker logs mvs-container

# Stop the container
docker stop mvs-container

# Remove the container
docker rm mvs-container
```

---

