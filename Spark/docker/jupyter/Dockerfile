FROM spark-base

ARG shared_workspace=/opt/workspace
ARG jupyterlab_version="3.0.0"

RUN mkdir workspace/

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install wget==3.2 jupyterlab==${jupyterlab_version}

EXPOSE 8888

WORKDIR /workspace
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=