
# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in environment.yml
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Ensure the conda environment is activated when the container starts
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Run app.py when the container launches
CMD ["python", "src/app.py"]
