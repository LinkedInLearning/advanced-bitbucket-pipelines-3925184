# 01_03 Configure resource allocation

We can use the `size` option to allocate additional CPU, memory, and storage for an entire pipeline, or for a specific step.

- Pipeline:

```yaml
options:
  size: 2x
pipelines:
  default:
	- step:
    	…
```

- Step:

```yaml
- step:
    size: 2x
    script:
      - …
```

The `size` option can be set to one of the following values:

| Size | RAM    | CPU           | Disk   |
|------|--------|---------------|--------|
| 1x   | 4 GB   | 4 Shared      | 64 GB  |
| 2x   | 8 GB   | 4 Shared      | 64 GB  |
| 4x   | 16 GB  | 8 Dedicated   | 256 GB |
| 8x   | 32 GB  | 16 Dedicated  | 256 GB |

> [!IMPORTANT]
> 4x and 8x sizes are only available for Bitbucket accounts associated with a paid plan.


> [!WARNING]
> Increasing size uses additional build minutes.
> 2x, 4x, and 8x will use the same multiplier on build minutes per minute of execution


>


<!-- FooterStart -->
---
[← 01_02 Configure Maximum Runtime](../01_02_configure_maximum_runtime/README.md) | [Advanced Bitbucket Pipelines: Automating Deployments & Managing Third Party Integrations →](../../README.md)
<!-- FooterEnd -->
