## DevOps Simple Demo (FastAPI + Docker + GitHub Actions)

This is a minimal sample project to practice a basic DevOps flow:

1. Build a Docker image for a FastAPI app
2. Verify it in CI (GitHub Actions) by calling `GET /health`

### How to run locally

```bash
docker build -t devops-demo-orbit7 ./devops-demo-orbit7
docker run --rm -p 8000:8000 devops-demo-orbit7
```

Then open:
- `http://localhost:8000/` (welcome message)
- `http://localhost:8000/health` (health check JSON)

### CI (GitHub Actions)

The workflow lives in `.github/workflows/ci.yml` and runs on:
- `push`
- `pull_request`

It will:
- build the Docker image
- start a container
- `curl` the `/health` endpoint to confirm it responds

