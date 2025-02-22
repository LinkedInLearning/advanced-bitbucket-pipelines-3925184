# 03_05 Use a custom pipe in a pipeline

If you followed along with the previous lessons to:

- create a custom pipe
- and push the pipe to a container registry

Create a Bitbucket Pipelines configuration that uses the pipe.

Your configuration should be similar to the following:

```yaml
image: atlassian/default-image:4

pipelines:
  default:
    - step:
        name: Test Custom Pipe
        script:
          - pipe: YOUR_USER_NAME_HERE/YOUR_PIPE_NAME_HERE:PIPE.VERSION.HERE
            variables:
              NAME: "$BITBUCKET_REPO_OWNER" # Or any other variables that your pipe needs
```

## Shenanigans

### 03_05.1: The Log Output for the Custom Pipe may be Truncated

When the custom pipeline developed in the previous lesson is run, the output from the log is cut off.

No worries!  Just refresh the browser window and take another look.

![You're AWESOME!](./images/00-youre-awesome.png)

<!-- FooterStart -->
---
[← 03_04 Deploy a Custom Pipe to a Container Registry](../03_04_deploy_a_custom_pipe_to_a_container_registry/README.md) | [03_06 Challenge: Develop a Custom Pipe →](../03_06_challenge_create_a_custom_pipe/README.md)
<!-- FooterEnd -->
