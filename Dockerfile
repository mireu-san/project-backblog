# Use an official Python runtime as a parent image
FROM python:3.10-alpine3.18
LABEL maintainer="https://github.com/mireu-san"

# To run in docker container - in order to not buffer the output
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container at /app
COPY ./requirements.txt /tmp/requirements.txt
# Copy the current directory contents into the container at /app
COPY ./app /app
# Set the working directory to /app
WORKDIR /app
# Expose port 8000 for the Django app
EXPOSE 8000

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]