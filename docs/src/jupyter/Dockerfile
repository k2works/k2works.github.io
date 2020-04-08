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
    ca-certificates

# Pandoc
RUN apt-get update && \
    apt-get install -y pandoc

# PluntUML
RUN apt-get update && \
    apt-get install -y default-jdk graphviz fonts-takao
RUN wget 'https://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=http%3A%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' && \
    mv 'plantuml.jar?r=http%3A%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' /usr/local/bin/plantuml.jar
COPY ./plantuml.sh /usr/local/bin/plantuml
RUN chmod a+x /usr/local/bin/plantuml

# Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libbz2-dev \
    libsqlite3-dev \
    libreadline-dev \
    zlib1g-dev \
    libasound2-dev \
    libxss1 \
    libxtst6 \
    libffi-dev

ENV PYTHON_VER 3.7.0
ENV HOME /root
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
RUN echo 'export PATH="/$HOME/.pyenv/bin:$PATH"' >> $HOME/.bash_profile
RUN echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bash_profile
RUN . $HOME/.bash_profile && \
    pyenv install $PYTHON_VER  && \
    pyenv global $PYTHON_VER
ENV PATH $HOME/.pyenv/shims:$PATH
RUN pip install --upgrade pip && \
    pip install jupyter && \
    pip install sphinx && \
    pip install sphinx-autobuild && \
    pip install nbsphinx && \
    pip install sphinx_rtd_theme && \
    pip install sphinxcontrib-plantuml && \
    pip install RISE && \
    pip install jupyter-contrib-nbextensions && \
    pip install jupyter-nbextensions-configurator && \
    pip install autopep8 && \
    pip install numpy && \
    pip install pandas && \
    pip install matplotlib

# jupyter-vim-binding
# Create required directory in case (optional)
RUN mkdir -p $(jupyter --data-dir)/nbextensions
# Clone the repository
RUN cd $(jupyter --data-dir)/nbextensions && \
    git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
# Activate the extension
RUN jupyter nbextension enable vim_binding/vim_binding

# RISE
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

# 拡張機能を有効化する
RUN jupyter contrib nbextension install
RUN jupyter nbextensions_configurator enable

# autopep8
RUN jupyter nbextension install https://github.com/kenkoooo/jupyter-autopep8/archive/master.zip --user
RUN jupyter nbextension enable jupyter-autopep8-master/jupyter-autopep8

# 日本語拡張
RUN pip install japanize-matplotlib