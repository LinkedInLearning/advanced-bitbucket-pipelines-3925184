# 04_07 Challenge: Deploy a Self-Hosted Runner

## Challenge Scenario

In this challenge you’re continuing your role as the Bitbucket Pipelines expert supporting the Amazing Mobile App.

The Amazing Mobile App’s DevOps team needs to run a deployment script that accesses sensitive data stored in the company's AWS account.  The deployment script needs to access AWS Parameter Store to retrieve the path to the file that contains the data.

They're concerned about the risk of enabling Bitbucket's runners to have access to private networks and would like to develop a solution that uses their own, self-hosted runners.

Before building out their solution, they've asked you to develop a proof of concept that shows how a workflow running in Bitbucket Pipelines can access protected resources in AWS using a self-hosted runner.

## Challenge Tasks

Complete the following steps to solve this challenge:

1. Use the exercise files to deploy resources that model the needs of the DevOps team.

    **NOTE: If you are following along with the course and have deployed the resources described in [04_04 Deploy an EC2 Server in AWS](../04_04_deploy_an_ec2_server_in_aws/README.md), then you can skip this step.  Those resources can be reused for this challenge.**

    ![AWS Resources](./images/cfn-designer.png)

    The resources include:

    1. A parameter store location that contains the path to a data file
    1. An IAM policy and role that allow an EC2 instance to read the parameter
    1. An EC2 instance that assumes the role and can be used as a self-hosted runner

1. Deploy a runner on the EC2 instance using the runner type that is most applicable to the needs of the DevOps team.

    **NOTE: If you are following along with the course and have deployed the resources described in [04_05 Install Runners in a Workspace](../04_05_install_runners_in_a_workspace/), then you can skip this step.  Those runners can be reused for this challenge.**

    - What type of runner should you deploy; **Linux Shell** or **Linux Docker**?
    - Why is the runner you selected the right choice for your solution?

1. Create a new repository, add the exercise files, and create repository variables. This includes:

    1. A script that will read a Parameter Store location and then read a data file.
    1. A pipeline configuration that schedules a step to run on a self-hosted runner and then runs the script.
    1. A repository variable named `AWS_REGION` that contains the region where the runner was deployed.

1. Confirm that the runner you deployed and the repository configuration validate the proof of concept.

This challenge should take 25-30 minutes to complete.

<!-- FooterStart -->
---
[← 04_06 Use Self-Hosted Runners in a Pipeline](../04_06_use_self_hosted_runners_in_a_pipeline/README.md) | [04_08 Solution: Deploy a Self-Hosted Runner →](../04_08_solution_deploy_a_self_hosted_runner/README.md)
<!-- FooterEnd -->
