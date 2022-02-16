# The image to base the container on, lets use the official python runtime as a parent image
FROM python:3.7

# Set working directory
WORKDIR /app

# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Add requirements
COPY ./requirements.txt /app/requirements.txt

# Install Requirements
RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . /app

EXPOSE 8000

# Runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
