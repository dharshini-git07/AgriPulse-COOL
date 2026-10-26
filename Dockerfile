# Use Ubuntu 24.04 LTS ARM64 base compatible with AWS Graviton & COOL AMIs
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python3", "src/app.py"]