# Lucina

Lucina is a project to centralize employee photos for usage in integrated workflows, web applications and email signatures.

## Automation

This repository uses workflows in the `.github/workflows` directory

- `release.yml` - Generates a new build on pushes to the main branch. If necessary, a new version
is released.

### Secrets Management

Some actions secrets are used inside the repository settings:

- `GITHUB_TOKEN` - Github PAT used to publish releases and tags

## Project Documentation

Additional documentation for the Numigi Lucina project can be found at [docs.numi.tools](https://docs.numi.tools).
