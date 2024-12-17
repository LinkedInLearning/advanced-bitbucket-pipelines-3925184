# Bitbucket Pipelines Pipe: example

example

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
script:
  - pipe: example/example:0.0.0
    variables:
      NAME: "<string>"
      # DEBUG: "<boolean>" # Optional
```
## Variables

| Variable | Usage                                              |
|----------|----------------------------------------------------|
| NAME (*) | The name that will be printed in the logs          |
| DEBUG    | Turn on extra debug information. Default: `false`. |

_(*) = required variable._

## Prerequisites

## Examples

Basic example:

```yaml
script:
  - pipe: example/example:0.0.0
    variables:
      NAME: "foobar"
```

Advanced example:

```yaml
script:
  - pipe: example/example:0.0.0
    variables:
      NAME: "foobar"
      DEBUG: "true"
```

## Support
If you’d like help with this pipe, or you have an issue or feature request, let us know.
The pipe is maintained by example.

If you’re reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce

## License
Copyright (c) 2019 Atlassian and others.
Apache 2.0 licensed, see [LICENSE](LICENSE.txt) file.

<!-- FooterStart -->
---
[← 03_02 Develop a Custom Pipe](../README.md) | [Bitbucket Pipelines Pipe: example →](../advanced-python/README.md)
<!-- FooterEnd -->
