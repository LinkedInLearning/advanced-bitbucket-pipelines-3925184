# 00_04 Bitbucket Pipelines Review

You should be familiar with these essential elements of the Bitbucket Pipelines configuration:

| Element | Notes | Reference |
|---------|-------|-------|
| `bitbucket-pipelines.yml`| The Pipelines configuration file where the CI/CD process is defined in YAML format. | [Bitbucket Pipelines configuration reference](https://support.atlassian.com/bitbucket-cloud/docs/bitbucket-pipelines-configuration-reference/) |
| Triggers | Define events that start pipelines (e.g., `push`, `pull request`, `tags`, `custom`). | [Pipeline start conditions](https://support.atlassian.com/bitbucket-cloud/docs/pipeline-start-conditions/) |
| Image | Specifies the Docker image used as the environment for the pipeline's execution. | [Docker image options](https://support.atlassian.com/bitbucket-cloud/docs/docker-image-options/) |
| Steps | Define individual tasks in a pipeline, executed sequentially within a stage. | [Step Options](https://support.atlassian.com/bitbucket-cloud/docs/step-options/) |
| Stages | Group steps into logical units to organize and parallelize pipeline execution. | [Stage Options](https://support.atlassian.com/bitbucket-cloud/docs/stage-options/) |
| YAML Anchors | Reusable YAML syntax to avoid duplication, useful for defining shared steps or configurations. | [YAML Anchors](https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/) |


<!-- FooterStart -->
---
[← 00_03 Using the Exercise Files](../00_03_using_the_exercise_files/README.md) | [01_01 Optimizing Pipeline Performance and Reducing Build Times →](../../ch1_pipeline_optimizations/01_01_optimizing_pipeline_performance/README.md)
<!-- FooterEnd -->
