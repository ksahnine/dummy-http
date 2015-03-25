# Build:
#   docker build -t ksahnine/dummy-http .
#
# Run: 
#   docker run -t -p 8080:8080 ksahnine/dummy-http
#
# DOCKER_VERSION 1.5

FROM google/python
MAINTAINER Kadda SAHNINE <kadda.sahnine@inovia-conseil.fr>

ADD dummyhttp.py /app/dummyhttp.py

CMD []
ENTRYPOINT ["python", "/app/dummyhttp.py"]

EXPOSE 8080
