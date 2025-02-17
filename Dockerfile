# Use an official Python runtime as a parent image
FROM python:3.12-alpine

EXPOSE 8000
# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /code
COPY . /app

RUN pip install uv

RUN uv pip install twisted[tls,http2] --system

# Install dependencies
RUN uv pip install -r requirements.txt --system # --no-cache-dir


RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# RUN echo 'appuser ALL=(ALL) NOPASSWD: ALL' >  /etc/sudoers.d/appuser
USER appuser

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]