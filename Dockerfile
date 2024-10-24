
# The first instruction is what image we want to base our container on

# We Use an official Python runtime as a parent image

FROM python
 
# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1
 
# Set the working directory in the container

WORKDIR /code
 
# Copy the requirements file to the working directory

COPY requirements.txt /code/
 
# Install project dependencies

RUN pip install --upgrade pip
 
# Copy the project code to the working directory

COPY . /code/
 
# Run migrations

#RUN python manage.py migrate
 
# Expose port 8000 for the Django development server

EXPOSE 8000
 
# Start the Django development server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]