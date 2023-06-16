# Lucina

Lucina is a project to centralize employee photos for usage in integrated workflows, web applications and email signatures.

## Contributing

See `CONTRIBUTING.md` for ways to get started.

## Automation

This repository uses multiple workflows in the `.github/workflows` directory

- `auto-create-release.yml` - Creates a release on changes in the `package.json`
- `auto-create-tag.yml` - Creates a tag on changes in the `package.json`

### Secrets Management

Some actions secrets are used inside the repository settings:

- `GITHUB_TOKEN` - Github PAT used to publish releases and tags
- `PERSONAL_TOKEN` - Github PAT used to publish releases and tags

## Project Documentation

Additional documentation for the Numigi Lucina project can be found at [docs.numi.tools](https://docs.numi.tools).
