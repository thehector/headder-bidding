FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /bidders/requirements.txt
WORKDIR /bidders
RUN pip install -r requirements.txt
COPY . /bidders
ENTRYPOINT [ "python" ]
CMD [ "bidder.py" ]
