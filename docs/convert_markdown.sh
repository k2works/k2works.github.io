docker image build -t k2works/pandoc:latest .
docker container run -v $(pwd):/docs/ k2works/pandoc:latest asciidoctor -b docbook  docs/src/asciidoc/index.adoc
docker container run -v $(pwd):/docs/ k2works/pandoc:latest pandoc -f docbook -t gfm docs/src/asciidoc/index.xml -o /docs/src/asciidoc/index.md
docker container run -v $(pwd):/docs/ k2works/pandoc:latest iconv -t utf-8 /docs/src/asciidoc/index.xml | pandoc -f docbook -t gfm | iconv -f utf-8 > ./src/asciidoc/index.md
docker container run -v $(pwd):/docs/ k2works/pandoc:latest pandoc -f docbook -t gfm --wrap=none
docker container run -v $(pwd):/docs/ k2works/pandoc:latest pandoc -f docbook -t gfm --columns=120

# https://gist.github.com/cheungnj/38becf045654119f96c87db829f1be8e
