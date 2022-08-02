FROM python:3.10
RUN apt-get update && apt-get install graphviz graphviz-dev --assume-yes
RUN mkdir siit
WORKDIR /siit
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /siit
ENTRYPOINT [ "./docker_entrypoint.sh" ]
EXPOSE 8000