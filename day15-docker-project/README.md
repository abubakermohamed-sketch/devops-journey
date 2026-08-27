# Day 15: Dockerized Inventory Reporter

Containerized the Day 5 server inventory classifier using Docker.

## What it does
Reads `inventory.txt`, classifies each server by type, writes results to `report.txt` — now running inside an isolated Docker container instead of directly on the host machine.

## Usage
```bash
docker build -t inventory-reporter .
docker run inventory-reporter
```

## What I learned
- Images vs. containers, and why containers are lightweight compared to VMs
- Container filesystem isolation — files created inside a container don't automatically appear on the host
- Image immutability — rebuilding is required to pick up local code changes
- Dockerfile basics: FROM, WORKDIR, COPY, CMD
- `docker cp` to extract files from a stopped container
