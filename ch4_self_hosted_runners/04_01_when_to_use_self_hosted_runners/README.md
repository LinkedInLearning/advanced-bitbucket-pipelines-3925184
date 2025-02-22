# 04_01 When to Use Self-Hosted Runners

Self-hosted runners give you greater control and customization for your CI/CD pipelines compared to Atlassian’s cloud-hosted runners.

Following are the key points we'll explore in this chapter:

- **Enhanced Control & Customization:**  You can tailor hardware (CPU, memory, storage) and build environments to meet demanding or specialized requirements.

- **Security & Compliance:**  Running pipelines on private infrastructure allows secure interactions with internal networks and helps safeguard sensitive data to meet regulations like GDPR and HIPAA.

- **Cost Advantages:**  Since build minutes aren’t charged on your own infrastructure and data transfer stays internal, self-hosting can reduce costs for long-running or frequent jobs.

- **Operational Challenges:**  Self-hosting requires you to manage server deployment, maintenance, scalability, and regular security updates. It also introduces security risks, so it’s recommended only for private repositories and environments with strict access controls.

- **When to Consider Self-Hosting:**  It’s a good fit if you encounter resource limitations on the cloud, have dedicated infrastructure available, need to work with sensitive or internal systems, and are prepared to manage the associated maintenance and security responsibilities.

Now let's discuss how to deploy and use self-hosted runners in your pipelines.

## References

- [Set up runners for Linux Shell](https://support.atlassian.com/bitbucket-cloud/docs/set-up-runners-for-linux-shell/)
- [Set up runners for Linux Docker](https://support.atlassian.com/bitbucket-cloud/docs/set-up-and-use-runners-for-linux/)

<!-- FooterStart -->
---
[← 03_07 Solution: Develop a custom pipe](../../ch3_create_custom_pipes/03_07_solution_create_a_custom_pipe/README.md) | [04_02 Self-Hosted Runner Configurations →](../04_02_self_hosted_runner_configurations/README.md)
<!-- FooterEnd -->
