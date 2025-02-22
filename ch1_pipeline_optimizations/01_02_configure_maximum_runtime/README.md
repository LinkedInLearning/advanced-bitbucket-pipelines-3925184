# 01_02 Configure Maximum Runtime

## Reference

[Max Time](https://support.atlassian.com/bitbucket-cloud/docs/global-options/#Max-time)

The max-time option sets the maximum length of time a step can run before timing out (in minutes). The max-time option can be set using both the global options property and on individual pipeline steps. The default maximum time for pipeline steps is 120 minutes.

## Pipeline Setting

```yaml
options:
  max-time: 2 # The entire pipeline will timeout after 2 minutes
```

## Step Setting

```yaml
- step:
    max-time: 2
    script:
        -  sleep 120m # This step will timeout after 2 minutes
```

## Using the Exercise Files

1. Create a new repo and add the exercise files
1. Adding the files may not trigger the pipeline right away.  Go to the **Pipelines** menu and select **Run initial pipeline**.
1. Observe the pipeline being stopped after the amount of time specified in the pipeline configuration.

<!-- FooterStart -->
---
[← 01_01 Optimizing Pipeline Performance and Reducing Build Times](../01_01_optimizing_pipeline_performance/README.md) | [01_03 Configure resource allocation →](../01_03_configure_resource_allocation/README.md)
<!-- FooterEnd -->
