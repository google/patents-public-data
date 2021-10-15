FROM index.docker.io/library/debian:stable-slim

RUN apt-get update

RUN apt-get install -y wget build-essential

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

RUN bash ./Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local

RUN conda create -n beam-env python=3.8

# Run the next commands inside the conda environment.
RUN conda init bash
RUN echo "conda activate beam-env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

RUN conda install -q -y -c conda-forge rdkit pip

RUN pip install --no-cache-dir apache-beam[gcp]==2.31.0

# Copy files from official SDK image, including script/dependencies
COPY --from=registry.hub.docker.com/apache/beam_python3.8_sdk:2.31.0 /opt/apache/beam /opt/apache/beam

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "beam-env", "/opt/apache/beam/boot"]
