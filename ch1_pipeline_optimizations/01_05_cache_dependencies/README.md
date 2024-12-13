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


<!-- FooterStart -->
---
[← 01_04 Use Conditional Steps](../01_04_use_conditional_steps/README.md) | [Advanced Bitbucket Pipelines: Automating Deployments & Managing Third Party Integrations →](../../README.md)
<!-- FooterEnd -->
