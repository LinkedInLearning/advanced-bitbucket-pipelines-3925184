# 04_03 Compare Repository and Workspace Runners

Self-hosted runners can be set up at the repository level for dedicated, consistent environments or at the workspace level to share resources across multiple projects.

- Repo-level runners are ideal for custom environments (like Linux-shell, Windows, or macOS).
- Workspace runners, especially using Linux-Docker, prevent dependency conflicts by providing isolated environments for each run.

| Repository Runners                   | Workspace Runners |
|--------------------------------------|-------------------|
| Runner access is limited to the repo | Runner is available to all repos in the workspace |
| Linux Shell, Windows, and macOS Runners | Linux Docker |
| Tools, dependencies, and hardware are consistent | Creates clean environments on each run |

<!-- FooterStart -->
---
[← 04_02 Self-Hosted Runner Configurations](../04_02_self_hosted_runner_configurations/README.md) | [04_04 Deploy an EC2 Server in AWS →](../04_04_deploy_an_ec2_server_in_aws/README.md)
<!-- FooterEnd -->
