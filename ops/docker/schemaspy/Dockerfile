FROM schemaspy/schemaspy:6.2.2
USER root
WORKDIR /
RUN apk update && \
    apk add --no-cache curl fontconfig && \
    mkdir download && \
    cd download && \
    curl -O https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip && \
    unzip IPAexfont00401.zip && \
    mkdir -p /usr/share/fonts/truetype/ipa && \
    cp */*ttf /usr/share/fonts/truetype/ipa && \
    fc-cache -fv && \
    rm -rf download

# https://dev.classmethod.jp/articles/schemaspy-docker-localize-jp/
