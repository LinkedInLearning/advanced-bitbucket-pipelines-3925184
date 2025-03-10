# 01_05 Cache Dependencies

**Dependencies**: external components that a software application
relies on to function properly.

- Examples:
  - Python script that needs data analysis capabilities may depend on the [pandas](https://pandas.pydata.org/) library.
  - Javascript web application that needs a graphical interface may depend on the [React](https://react.dev/) framework.

## Caching dependencies in pipelines

```yaml
- step:
    caches:
      - CACHE_NAME_1
      - CACHE_NAME_2
```

### Pre-defined caches

- `docker`
- `composer`
- `dotnetcore`
- `gradle`
- `ivy2`
- `maven`
- `node`
- `pip`
- `sbt`

### Custom caches

Define the cache in the `definitions` section:

- `path`: identifies where dependencies are stored
- `key` and `files`: the files to check for changes to determine if the cache needs to be recreated. Multiple files can be listed.

```yaml
definitions:
  caches:
    custom-ruby:
      path: ruby-backend/vendor/bundle
      key:
        files:
          - ruby-backend/Gemfile.lock
```

Then use the cache by name in a `step`:

```yaml
- step:
    name: Test Ruby
    caches:
        - custom-ruby
```

## References

- Compressed cache size limit is 1 GB; Any larger and the cache will not be uploaded.

- [Caches - Step Options](https://support.atlassian.com/bitbucket-cloud/docs/step-options/#Caches)
- [Caches - Documentation](https://support.atlassian.com/bitbucket-cloud/docs/cache-dependencies/)

## Using the Exercise Files

1. The lesson reuses the repo and exercise files from [01_04 Use Conditional Steps](../01_04_use_conditional_steps/README.md).
1. Replace the contents of the pipeline configuration with the contents of the `bitbucket-pipelines.yaml` from this lesson.
1. Observe the pipeline activity after committing the new pipeline configuration.
1. Make a change to a file in `ruby-backend`, such as adding a comment.
1. Observe the pipeline activity after committing the updated file.

<!-- FooterStart -->
---
[← 01_04 Use Conditional Steps](../01_04_use_conditional_steps/README.md) | [01_06 Challenge: Optimize a Workflow in Bitbucket Pipelines →](../01_06_challenge_optimize_a_pipeline/README.md)
<!-- FooterEnd -->
