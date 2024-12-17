# 03_01 When to Use Custom Pipes

## Reasons to Create a Custom Pipe

- Developing pipelines that perform the same, complex tasks in several steps or need to run complex tasks across multiple repositories
- Vendor that wants developers to integrate with their software or platform from Bitbucket Pipelines
- Advanced pipeline solutions with specific dependencies or complex environments

## Simple Pipe vs Complete Pipe

- **Simple pipes** are intended for personal and team use and require:
  - A script
  - A Dockerfile
  - Image deployment and hosting

- **Complete pipes**  are intended for public use and distribution. In addition to the simple pipe requirements, complete pipes require:
  - A metadata file
  - Documentation
  - A test suite

> [!IMPORTANT]
> Only complete pipes may be considered for distribution via the Atlassian Marketplace.

## Pipe Development Tools and Resources

| Resource | Link |
|----------|------|
| Official documentation for creating Bitbucket Pipes | [Write a pipe for Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/write-a-pipe-for-bitbucket-pipelines/) |
| A Yeoman generator for creating Bitbucket Pipes | [NPM: generator-bitbucket-pipes](https://www.npmjs.com/package/generator-bitbucket-pipe)<br>[Repo: bitbucket-pipe-release](https://bitbucket.org/atlassian/bitbucket-pipe-release/src/master/)|
| A Python library for developing Bitbucket Pipes | [bitbucket-pipes-toolkit](https://bitbucket.org/bitbucketpipelines/bitbucket-pipes-toolkit/src/master/) |
| A Bash library for developing Bitbucket Pipes | [bitbucket-pipes-toolkit-bash](https://bitbucket.org/bitbucketpipelines/bitbucket-pipes-toolkit-bash/src/master/) |
| A simple pipe example using Bash | [demo-simple-pipe](https://bitbucket.org/bitbucketpipelines/demo-pipe-simple/src/master/) |
| A complete pipe example using Python | [demo-pipe-python](https://bitbucket.org/atlassian/demo-pipe-python/src/master/) |
| Repositories for the Official Bitbucket Pipes | [Bitbucket Pipelines Pipes](https://bitbucket.org/atlassian/workspace/projects/BPP) |

<!-- FooterStart -->
---
[← 02_06 Solution: Use Pipes in a Pipeline](../../ch2_using_pipes_in_pipelines/02_06_solution_use_pipes_in_a_pipeline/README.md) | [03_02 Develop a Custom Pipe →](../03_02_develop_a_custom_pipe/README.md)
<!-- FooterEnd -->
