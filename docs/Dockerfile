FROM ubuntu:16.04

## Japanese
RUN apt-get update && \
    apt-get install -y language-pack-ja-base \
    language-pack-ja

RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# Base
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    git \
    ca-certificates \
    unzip \
    zip

# asciidoctor

RUN apt-get install asciidoctor -y

# Pandoc

RUN wget https://github.com/jgm/pandoc/releases/download/2.0.0.1/pandoc-2.0.0.1-1-amd64.deb
RUN dpkg -i pandoc-2.0.0.1-1-amd64.deb

# PluntUML
RUN apt-get install -y default-jdk gradle graphviz fonts-takao
RUN wget 'https://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=http%3A%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' && \
    mv 'plantuml.jar?r=http%3A%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' /usr/local/bin/plantuml.jar
COPY ./plantuml.sh /usr/local/bin/plantuml
RUN chmod a+x /usr/local/bin/plantuml