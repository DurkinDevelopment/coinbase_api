# Dockerfile

# The image to base the container on, lets use the official python runtime as a parent image
FROM python:3.7

# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

# Cleanup files to not clutter the final image
RUN rm requirement.txt

# Mounts the application code to the image
COPY . /app
WORKDIR /app

EXPOSE 8000

# Runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
