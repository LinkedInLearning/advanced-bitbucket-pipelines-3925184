# 04_08 Solution: Deploy a Self-Hosted Runner

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
    1. A repository variable that contains the region where the runner was deployed.

1. Confirm that the runner you deployed and the repository configuration validate the proof of concept.

This challenge should take 25-30 minutes to complete.

## Solution

1. **Deploy an EC2 Server**.

    - Follow the steps in [04_04 Deploy an EC2 Server in AWS](../04_04_deploy_an_ec2_server_in_aws/README.md) to deploy a server where runners can be installed.

1. **Install a Linux Shell runner**.

    - Follow the steps in [04_05 Install Runners in a Workspace](../04_05_install_runners_in_a_workspace/) to install a Linux Shell runner.

1. **Create a new repo and add the exercise files**.

    - The exercise files include all the code needed for this challenge.

1. **Create a repository variable for AWS_REGION**

    - _Note: You will need to enable Bitbucket Pipelines or run an initial pipeline before creating repository variables._
    - View the **Outputs** tab of the CloudFormation stack.  Make a note of the value for `AwsRegion`.
    - In the repository settings, create an unsecured variable named `AWS_REGION`.  Add the value from the CloudFormation stack.

1. **Run the pipeline and view the output**.

    - Run the pipeline.
    - Confirm that the pipeline connects to the desired runner.
    - Confirm that the **Read Data File** step is able to read the file stored on the server.

<!-- FooterStart -->
---
[← 04_07 Challenge: Deploy a Self-Hosted Runner](../04_07_challenge_deploy_a_self_hosted_runner/README.md) | [05_01 Next Steps →](../../ch5_conclusion/05_01_next_steps/README.md)
<!-- FooterEnd -->
