# 02_06 Solution: Use Pipes in a Pipeline

## Challenge Scenario

In this challenge you’re continuing your role as the Bitbucket Pipelines expert supporting the Amazing Mobile App.

As planning begins for the next fiscal year, the CFO has come to you and asked if there's a way to get a report of the build minutes being used across all of the companies repositories.  Specifically, they need to know which builds are taking the longest amount of time and how many build minutes are being used.  They'd also like to capture this information on a regular basis.

Use your knowledge of Bitbucket Pipelines to automate a solution for the CFO.

## Challenge Tasks

1. Log into Bitbucket and create a new repository.
1. Create a repository access token that you can use to collect the desired information.  The token must have the following permissions:

    - `Repositories:Write`
    - `Pipelines:Read`

1. Store the token as a repository variable named `STATISTICS_ACCESS_TOKEN`.
1. Use the following script element to format the report name:

    ```bash
    export FILENAME="builds-statistics-$(date +%Y-%m-%d).txt"
    ```

1. Use the following pipes to generate and store the report:

    - [atlassian/bitbucket-build-statistics](https://bitbucket.org/atlassian/bitbucket-build-statistics/src/master/)

        ```yaml
        - pipe: atlassian/bitbucket-build-statistics:1.5.3
        variables:
          BITBUCKET_ACCESS_TOKEN: $STATISTICS_ACCESS_TOKEN
          FILENAME: "$FILENAME"
        ```

    - [atlassian/bitbucket-upload-file](https://bitbucket.org/atlassian/bitbucket-upload-file/src/master/)

        ```yaml
          - pipe: atlassian/bitbucket-upload-file:0.7.1
            variables:
              BITBUCKET_ACCESS_TOKEN: $STATISTICS_ACCESS_TOKEN
              FILENAME: "*.txt"
        ```

This challenge should take 10-15 minutes to complete.

## Solution

Create a new repository and add the exercise files.

1. Download the exercise files
1. Clone the Bitbucket repo
1. Move the files into your Bitbucket repo
1. Push the files up to Bitbucket

Run the pipeline once to make sure pipelines are enabled before proceeding.

### Create an Access Token

1. Select **Repository settings** -> **Access tokens** -> **Create Repository Access Token**.
1. Name the token `Statistics Collection`.
1. Select the permission to include:

    - `Repositories:Write`
    - `Pipelines:Read`

   Select **Create**.

1. Select this stacked squares icon for the first entry in the list of tokens to copy the token to my clipboard. Click out of the dialog.
1. Select **Repository variables**.
1. Paste the value for the access token into the second field and then enter the name `STATISTICS_ACCESS_TOKEN`. Select **Add**.

### Create the Pipeline Configuration

1. Edit the pipeline configuration.
1. Add a cache for `docker`.
1. Add the following script elements:

    1. export the filename as a variable using the format indicated in the challenge requirements
    1. add a pipe to generate the build statistics report
    1. add a pipe to write the report to the **Downloads** page in the repository

### Check the Results

1. Run the pipeline and confirm that the report is generated as expected.
1. From the left-side menu, select **Downloads**.
1. Select the most recently generated report and save it to your local system.
1. Review the contents of the report.

The completed pipeline should be similar to the following: [bitbucket-pipelines.yml](./bitbucket-pipelines.yml)

```yaml
image: atlassian/default-image:4

pipelines:
  default:
    - step:
        name: Collect Bitbucket Build Statistics
        caches:
          - docker
        script:

          - export FILENAME="builds-statistics-$(date +%Y-%m-%d).txt"

          - pipe: atlassian/bitbucket-build-statistics:1.5.3
            variables:
              BITBUCKET_ACCESS_TOKEN: $STATISTICS_ACCESS_TOKEN
              FILENAME: "$FILENAME"

          - pipe: atlassian/bitbucket-upload-file:0.7.1
            variables:
              BITBUCKET_ACCESS_TOKEN: $STATISTICS_ACCESS_TOKEN
              FILENAME: "*.txt"

        artifacts:
          - "*.txt"
```

And the build usage report should be simliar to the following:

```text
+------------------------------------------------------------------------------+
|                           Repository build details                           |
+-------------------------------+--------+----------------+--------------------+
| Repository                    | Builds | Build Duration | Build Minutes Used |
+-------------------------------+--------+----------------+--------------------+
| amazing_app/caches            |   24   |  0d 0h 7m 47s  |    0d 0h 7m 30s    |
| amazing_app/caches-2          |   2    |  0d 0h 1m 2s   |    0d 0h 1m 0s     |
| amazing_app/monorepo          |   10   |  0d 0h 2m 48s  |    0d 0h 2m 41s    |
| amazing_app/ch1-challenge     |   14   | 0d 0h 21m 29s  |   0d 0h 21m 23s    |
| amazing_app/ch1-solution      |   5    |  0d 0h 4m 30s  |    0d 0h 4m 28s    |
| amazing_app/pipes-first-look  |   22   | 0d 0h 11m 34s  |   0d 0h 11m 29s    |
| amazing_app/pipes-second-look |   44   | 0d 0h 40m 32s  |   0d 0h 42m 12s    |
| amazing_app/build-statistics  |   3    |  0d 0h 1m 50s  |    0d 0h 1m 48s    |
+-------------------------------+--------+----------------+--------------------+
```

<!-- FooterStart -->
---
[← 02_05 Challenge: Use Pipes in a Pipeline](../02_05_challenge_use_pipes_in_a_pipeline/README.md) | [Advanced Bitbucket Pipelines: Automating Deployments & Managing Third Party Integrations →](../../README.md)
<!-- FooterEnd -->
