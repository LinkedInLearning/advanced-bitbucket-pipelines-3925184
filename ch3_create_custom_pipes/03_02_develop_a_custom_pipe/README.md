# 03_02 Develop a Custom Pipe

## Using the Pipeline Generator

> [!IMPORTANT]
> Your local system will need to have [Node.js](https://nodejs.org/en) and the [NPM package manager](https://www.npmjs.com/) installed to use the pipeline generator.
>
> You should have a [Docker Hub](https://hub.docker.com/) account before proceeding.

The [generator-bitbucket-pipes](https://www.npmjs.com/package/generator-bitbucket-pipe) is useful for quickly getting started with pipe development.  Its as easy as `1`, `2`, `3`.

| # | Step  | Details / Commands |
|---|-------|--------------------|
|1| Use `npm` to install `yo` and `generator-bitbucket-pipes` | `npm install -g yo generator-bitbucket-pipe` |
|2| Create a Bitbucket repo andn clone it to your local system | `git clone git@bitbucket.org:WORKSPACE_NAME/REPO_NAME.git` |
|3| Run the generator inside the cloned repo | `yo bitbucket-pipe` |

The wizard will prompt you to create one of the following:

- New Simple Pipe (Bash)
- New Simple Pipe (Python)
- New Advanced Pipe (Bash)
- New Advanced Pipe (Python)

> [!IMPORTANT]
> At this time, the pipeline generator supports `bash` and `python` scripts.  However, it can still be used to generate the scaffolding needed to develop a pipe environment for other languages.
>
> Just update the `Dockerfile` to support the target runtime and remove other files as needed.

### Simple Pipe

Selecting **New Simple Pipe** will create the following files in the current directory:

| File                    | Description |
|-------------------------|-------------|
| bitbucket-pipelines.yml | Pipeline configuration for testing and deploying the pipe to Dockerhub |
| Dockerfile              | Docker configuration to create the pipe's image |
| pipe.sh or pipe.py      | A script template |
| requirements.txt        | Libraries to install for Python pipes |

### Complete / Advanced Pipe

> [!IMPORTANT]
> The "Advanced Pipe" is also known as the "Complete Pipe".

> [!WARNING]
> When the wizard asks _"What is the name of your Bitbucket account (e.g. my-account)?"_ Enter the **WORKSPACE** that contains the repo for the pipe.  Entering your Bitbucket account name will cause 404s in the  generated URLs for the pipe

> [!WARNING]
> The value you provide in response to _"What your repository name (e.g. ftp-deploy)?"_[^1] and _"What is your Docker Hub account (e.g. atlassian)?"_ will be used to generate the pipeline script for pushing the pipe image to a Docker Hub repository.  Edit the `bitbucket-pipelines.yml` to resolve any conflicts.

Selecting **New Advanced Pipe** will create the following files in the current directory:

| File                      | Description |
|---------------------------|-------------|
| bitbucket-pipelines.yml   | Pipeline configuration for testing and deploying the pipe to Dockerhub |
| Dockerfile                | Docker configuration to create the pipe's image |
| pipe.yml                  | Metadata file describing the pipe's inputs, outputs and configuration |
| pipe/pipe.sh or pipe.py   | Main pipe implementation script in Bash or Python |
| test/requirements.txt     | Test dependencies for Python-based test suites |
| test/test.bats or test.py | Test suite implementation in Bash or Python |
| requirements.txt          | Python package dependencies for Python-based pipes |
| LICENSE.txt               | License terms for the pipe |
| README.md                 | Documentation and usage instructions |
| RELEASING.md              | Instructions for releasing new versions |
| .editorconfig             | Code style configuration |
| .gitignore                | Git ignore patterns |

## Developing Your Pipe

After you have the pipe template files in place, modify the files as needed to implement your custom solution.

[^1]: That's Atlassian's grammar...not mine! :D ~MJ

<!-- FooterStart -->
---
[← 03_01 When to Use Custom Pipes](../03_01_when_to_use_custom_pipes/README.md) | [Advanced Bitbucket Pipelines: Automating Deployments & Managing Third Party Integrations →](../../README.md)
<!-- FooterEnd -->
