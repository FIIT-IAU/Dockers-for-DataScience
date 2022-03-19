FROM tensorflow/tensorflow:2.3.1

ARG DEBIAN_FRONTEND=noninteractive

LABEL version='0.1.0'
LABEL maintainer="Giang Nguyen <giang.nguyen@stuba.sk>"
LABEL description="Data Science stack"

ENV LANG C.UTF-8

WORKDIR /code

RUN apt-get update && \
    pip3 install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
