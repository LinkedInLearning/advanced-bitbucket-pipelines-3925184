# 01_03 Configure resource allocation

## Reference

[Size](https://support.atlassian.com/bitbucket-cloud/docs/global-options/#Size)

We can use the `size` option to allocate additional CPU, memory, and storage for an entire pipeline, or for a specific step.

## Pipeline Resource Allocation

```yaml
options:
  size: 2x

pipelines:
  default:
    - step:
```

## Step Resource Allocation

```yaml
- step:
    size: 2x
    script:
      - echo "This step will run on a 2x instance"
```

## Available Sizes

The `size` option can be set to one of the following values:

| Size | RAM    | CPU           | Disk   |
|------|--------|---------------|--------|
| 1x   | 2 GB   | 4 Shared      | 64 GB  |
| 2x   | 8 GB   | 4 Shared      | 64 GB  |
| 4x   | 16 GB  | 8 Dedicated   | 256 GB |
| 8x   | 32 GB  | 16 Dedicated  | 256 GB |

> [!IMPORTANT]
> 4x and 8x sizes are only available for Bitbucket accounts associated with a paid plan.

> [!WARNING]
> Increasing size uses additional build minutes.
> 2x, 4x, and 8x will use the same multiplier on build minutes per minute of execution

## Using the Exercise Files

1. Create a new repo and add the exercise files
1. Adding the files may not trigger the pipeline right away.  Go to the **Pipelines** menu and select **Run initial pipeline**.
1. Compare the runtimes of the steps that use different size runners.

<!-- FooterStart -->
---
[← 01_02 Configure Maximum Runtime](../01_02_configure_maximum_runtime/README.md) | [01_04 Use Conditional Steps →](../01_04_use_conditional_steps/README.md)
<!-- FooterEnd -->
