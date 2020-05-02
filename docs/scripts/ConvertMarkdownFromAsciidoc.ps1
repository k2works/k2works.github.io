Start-Process -FilePath Docker -ArgumentList "image build -t k2works/pandoc:latest ./docs" -Wait

$path = (Convert-Path .) + '/docs'
$articles = @{
    'tdd_itddd' = @('index', '01_value_object', '02_entity')
}

foreach ($k in $articles.Keys) {
    $dir = "${path}/src/markdown"
    if (-not(Test-Path "${dir}")) { New-Item "${dir}" -ItemType Directory }
    if (-not(Test-Path "${dir}/${k}")) { New-Item "${dir}/${k}" -ItemType Directory }
}

foreach ($k in $articles.Keys) {
    foreach ($v in $articles[$k]) {
        $args = "container run -v ${path}:/docs/ k2works/pandoc:latest asciidoctor -b docbook  docs/src/asciidoc/${k}/${v}.adoc"
        Start-Process -FilePath Docker -ArgumentList $args -Wait
    }
    foreach ($v in $articles[$k]) {
        $args = "container run -v ${path}:/docs/ k2works/pandoc:latest pandoc -f docbook -t gfm docs/src/asciidoc/${k}/${v}.xml -o /docs/src/markdown/${k}/${v}.md"
        Start-Process -FilePath Docker -ArgumentList $args -Wait
    }
    foreach ($v in $articles[$k]) {
        $args = "container run -v ${path}:/docs/ k2works/pandoc:latest iconv -t utf-8 /docs/src/asciidoc/${k}/${v}.xml | pandoc -f docbook -t gfm | iconv -f utf-8 > ./src/markdown/${k}/${v}.md"
        Start-Process -FilePath Docker -ArgumentList $args -Wait
    }
}
