FROM python:3.11-slim

WORKDIR /docs

# Install MkDocs and necessary plugins
RUN pip install --no-cache-dir \
    mkdocs \
    mkdocs-material \
    pymdown-extensions \
    plantuml-markdown

# Copy configuration and docs
COPY mkdocs.yml /docs/
COPY docs/wiki /docs/docs/

# Expose the MkDocs development server port
EXPOSE 8000

# Start MkDocs development server
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
