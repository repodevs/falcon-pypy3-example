FROM pypy:3
MAINTAINER Edi Santoso "me@repodevs.com"

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

