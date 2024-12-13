# 01_04 Use Conditional Steps

- **Monorepos** are single repositories with code from multiple projects
- Inefficient CI/CD for monorepos can cause long pipeline runtimes and waste build minutes processing code that hasn't changed

## Using conditions to skip stages and steps

- [Pipeline Flow Control](https://support.atlassian.com/bitbucket-cloud/docs/step-options/#Flow-control)

Bitbucket allows us to use a `condition` directive to run portions of a pipeline if certain files have changed.

- Use [glob patterns](https://support.atlassian.com/bitbucket-cloud/docs/use-glob-patterns-on-the-pipelines-yaml-file/) to target individual files or directories
- If the event that triggered the pipeline includes changes to the indicated files or files inside the indicated directory, then the stage or step will be run.  Otherwise it gets skipped completely.

### Conditions in stages

```yaml
- stage:
    name: Cloud Deployment
    condition:
      changesets:
        includePaths:
          - "infrastructure/*.tf"\
```

### Conditions in steps

```yaml
- step:
    name: Test Python
    condition:
    changesets:
        includePaths:
          - "python-backend/**"
```

## Working with conditional pipelines

- This directory contains the following files that represent a monorepo.
- Use them to experiment with applying conditionals in a pipeline

```text
├── README.md
├── bitbucket-pipelines.yml
├── bitbucket-pipelines-no-conditional-steps.yml
├── bitbucket-pipelines-with-conditional-steps.yml
├── python-backend
│   ├── app.py
│   ├── app_test.py
│   └── requirements.txt
├── ruby-backend
│   ├── app.rb
│   ├── app_test.rb
│   └── Gemfile
│   └── Gemfile.lock
└── shared
    └── database-schema.json
```

<!-- FooterStart -->
---
[← 01_03 Configure resource allocation](../01_03_configure_resource_allocation/README.md) | [01_05 Cache Dependencies →](../01_05_cache_dependencies/README.md)
<!-- FooterEnd -->
