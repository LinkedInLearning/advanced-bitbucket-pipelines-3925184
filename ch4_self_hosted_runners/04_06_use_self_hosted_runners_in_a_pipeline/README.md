# 04_06 Use Self-Hosted Runners in a Pipeline

Follow the steps in the previous lessons to:

- Deploy an EC2 instance where self-hosted runners can be installed
- Install two self-hosted runners: a linux shell runner and a linux docker runner.

Then, create a new repo and added the exercise files for this lesson.

The [pipeline configuration](./bitbucket-pipelines.yml) sets up a script definition that can be used to explore the runners.

```yaml
definitions:
  script: &inspect-runner-environment
    - echo "Gathering CPU Info..." && lscpu
    - echo "Gathering Memory Info..." && free -h
    - echo "Disk Usage:" && df -h /
    - echo "Installed Tools:"
    - java --version || true
    - git --version  || true
    - docker --version  || true
    - echo "Listing All Commands:" && compgen -c
    - echo "Network Information:" && ip addr show
    - echo "Environment Variables:" && env

pipelines:
  default:
    - step:
        name: Use Linux Shell Runner
        runs-on:
          - self.hosted
          - linux.shell
          - os.al2023
        script: *inspect-runner-environment
    - step:
        name: Use Linux Docker Runner
        runs-on:
          - self.hosted
          - linux
        script: *inspect-runner-environment
```

Run the pipeline and compare the output from both runners.

> [!TIP]
> If you prefer not to run the pipeline for this lesson, use the following output for your review:
>
> - [Linux Shell Runner Output](./linux-shell-runner-pipelineLog.txt)
> - [Linux Docker Runner Output](./linux-docker-runner-pipelineLog.txt)

<!-- FooterStart -->
---
[← 04_05 Install Runners in a Workspace](../04_05_install_runners_in_a_workspace/README.md) | [04_07 Challenge: Deploy a Self-Hosted Runner →](../04_07_challenge_deploy_a_self_hosted_runner/README.md)
<!-- FooterEnd -->
