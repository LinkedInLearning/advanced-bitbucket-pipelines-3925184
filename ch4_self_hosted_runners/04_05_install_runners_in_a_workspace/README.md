# 04_05 Install Runners in a Workspace

Use the following references and instructions to install a Linux Docker runner and a Linux Shell runner in your Bitbucket workspace.

## References

- [Adding a new runner in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/adding-a-new-runner-in-bitbucket/)

## Install a Linux Docker Runner

1. **Prepare Your Environment**

    - Connected to the server that will host your runners.
    - Elevate your session to the root user account.
    - Verify that Java, Git, and Docker are installed and functioning correctly.  The following commands should run without error:

    ```bash
    java --version
    git --version
    docker --version
    ```

2. **Navigate to Workspace Runners**

    - Go to the Workspace Settings page in Bitbucket.
    - Scroll to the bottom of the left-hand menu and select **Workspace Runners**.

3. **Add a Runner**

    - Click the **Add Runner** button to start the installation wizard.

4. **Configure the Runner**

    - Select **Linux Docker** as the system and architecture.
    - Enter "Linux Docker" as the runner name.
    - Select **Next**.

5. **Copy the Docker Command**

    - Use the copy icon (stacked squares) to copy the command to your clipboard.

6. **Modify and Run the Docker Command**

    - Paste the command into your terminal.
    - Replace the `-it` flag with `--detach` to run the container in the background.
    - Run the command.

7. **Verify the Runner**

   - Run `docker ps` to get the container ID and confirm the container is running.
   - Use `docker logs -f <CONTAINER_ID>` to view the logs and confirm the runner is online.

8. **Complete the Setup in Bitbucket**

   - Return to Bitbucket, click **Next**, and follow the instructions to finalize the runner setup.

## Install a Linux Shell Runner

1. On the Workspace Settings page for Runners, click **Add Runner**.

    - Select **Linux Shell** as the system and architecture.

2. **Configure the Runner**

    - Enter "Linux Shell" as the runner name.
    - Add the label `os.al2023` to indicate Amazon Linux 2023 or, if you are using a different operating system for your runner, use a label that indicates that OS.
    - Click **Next**.

3. **Copy the Commands**

    - Copy the installation commands to your clipboard.

4. **Create and Run the Install Script**

   - Back in your terminal, create a file named `install.sh`:

        ```bash
        vim install.sh
        ```

   - Paste the installation commands into the file, save, and exit:

        - Press `i` to enter insert mode.
        - Paste the commands with `Ctrl+V`.
        - Exit insert mode with `Esc`, then type `:wq` to save and exit.

5. **Create and Run the Start Script**

    - Copy the start commands from the wizard.
    - Create a file named `run.sh` in your terminal:

        ```bash
        vim run.sh
        ```

    - Paste the start commands into the file, save, and exit using the same steps as above.
    - Make the scripts executable:

        ```bash
        chmod +x ./install.sh ./run.sh
        ```

6. **Run the Install Script**

    ```bash
    ./install.sh
    ```

7. **Start the Runner**

    - Start the runner in the background and redirect logs to an output file:

        ```bash
        nohup ./run.sh &> output.log &
        ```

    - Verify the script is running with:

        ```bash
        jobs
        ```

    - Check the logs:

        ```bash
        tail -f output.log
        ```

8. **Complete the Setup in Bitbucket**

    - Return to Bitbucket, click **Next**, and then **Finish** to complete the setup.

---

Now that both runners are online, you can use them in your Bitbucket pipelines.

<!-- FooterStart -->
---
[← 04_04 Deploy an EC2 Server in AWS](../04_04_deploy_an_ec2_server_in_aws/README.md) | [04_06 Use Self-Hosted Runners in a Pipeline →](../04_06_use_self_hosted_runners_in_a_pipeline/README.md)
<!-- FooterEnd -->
