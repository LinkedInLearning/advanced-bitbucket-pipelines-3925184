# 04_02 Self-Hosted Runner Configurations

Here are a few key points regarding self-hosted runners:

- **Runner Options:**  You can choose from Linux Docker, Linux Shell, Windows, or MacOS runners.

- **Common System Requirements:**  All runners require a 64-bit OS with at least 8 GB of RAM, a recent version of the Open Java Development Kit, and Git installed.

- **Runner Labels:**  Labels can be added to runners to specify characteristics like operating system or pre-installed tools, which helps in targeting the right runner for specific pipeline tasks.

- **Focus on Linux Options:**  The unit emphasizes Linux Docker and Linux Shell runners due to their broad applicability in CI/CD scenarios.

  - **Linux Docker Runners:**  They run steps in isolated container environments, ensuring a clean workspace for each pipeline run, though they don’t have access to the host file system.

  - **Linux Shell Runners:**  They operate in persistent environments that maintain state between steps, allowing for faster builds by using pre-installed tools and dependencies.

The upcoming lessons will cover deploying a server to experiment with these runner types.

## References


- https://support.atlassian.com/bitbucket-cloud/docs/set-up-runners-for-linux-shell/

<!-- FooterStart -->
---
[← 04_01 When to Use Self-Hosted Runners](../04_01_when_to_use_self_hosted_runners/README.md) | [04_03 Compare Repository and Workspace Runners →](../04_03_compare_repository_and_workspace_runners/README.md)
<!-- FooterEnd -->
