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


<!-- FooterStart -->
---
[← 02_06 Solution: Use Pipes in a Pipeline](../../ch2_using_pipes_in_pipelines/02_06_solution_use_pipes_in_a_pipeline/README.md) | [Advanced Bitbucket Pipelines: Automating Deployments & Managing Third Party Integrations →](../../README.md)
<!-- FooterEnd -->
