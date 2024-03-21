# FROM python:3.9-slim

# # 
# WORKDIR /code

# # 
# COPY . /code

# # 
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# EXPOSE 80

# # 
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

##############

FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
# ENV APP_HOME /app
# WORKDIR $APP_HOME 
# COPY . ./

WORKDIR /code
COPY . /code
 
# Install production dependencies.
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    pkg-config \
    gcc \
    python3-dev

RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT -k uvicorn.workers.UvicornWorker --timeout 0 main:app

# CMD ["uvicorn",  "main:app", "--port", "8000", "--host", "0.0.0.0"]

#######

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./your-path /app/your-path


