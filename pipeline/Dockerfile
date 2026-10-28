# Start with slim python 3.13 image
FROM python:3.13.11-slim

# Copy uv binary from official uv image (multistage build)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Setup working directory 
WORKDIR /code
# Activate virtual environment and install dependencies
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked 

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]