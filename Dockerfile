FROM centos:7.8.2003

MAINTAINER jelaiw@uab.edu

# Install Python 3.
RUN yum -y install python3

ENV APPROOT="/app"
ENV FLASK_APP="dev_server.py"
# See https://click.palletsprojects.com/en/7.x/python3/.
ENV LC_ALL="en_US.utf-8"
ENV LANG="en_US.utf-8"

WORKDIR $APPROOT

COPY dev_server.py $APPROOT
COPY requirements.txt $APPROOT

# Install Flask (peg to versions in requirements.txt).
RUN pip3 install -r requirements.txt

ENTRYPOINT ["flask", "run"]
