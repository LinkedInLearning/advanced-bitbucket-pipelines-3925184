# 03_06 Challenge: Develop a Custom Pipe

## Challenge Scenario

The world-renowned Amazing Mobile App is expanding!  Their new strategy will allow business partners to integrate with the mobile app directly from their deployment pipelines using APIs.

The initiative is led by the Amazing Library for Phone Hooks and APIs (ALPHA) Team. The ALPHA Team is planning to base the new integration on credentials that include an API key and a Customer ID.

Before implementing the API interface, the ALPHA team is asking you to demonstrate how customers can use a pipe to call the ALPHA API. They've asked you to update their code (which was generated using a Python-based Complete Pipe template) to use the `CUSTOMER_ID` parameter instead of the `NAME` parameter.

All the code you need for this challenge can be found in the exercise files for this lesson in the `./ALPHA-Team-Pipe` directory.

Review the notes in the following sections for the tools and techniques you’ll use to solve this challenge:

- [03_02 Develop a Custom Pipe](../03_02_develop_a_custom_pipe/README.md)
- [03_03 Test a custom pipe](../03_03_test_a_custom_pipe/README.md)

## Challenge Tasks

1. **Run the Test Suite**:

    After getting the files in place, run the `pytest` test suite to confirm that the code is working before you make any changes:

    ```bash
    pytest --verbose test/test*.py
    ```

1. **Explore the Provided Code**:

    Review the following files to see how the `NAME` parameter is being used and tested:

    - `pipe/pipe.py`
    - `test/test.py`

1. **Update the Code**:

    Complete the following:

    - Replace `NAME` with `CUSTOMER_ID` throughout the `pipe.py` file.
    - Adjust any associated variables as needed.
    - Update the success message to include the value of `CUSTOMER_ID`.  That is, for `CUSTOMER_ID=DEC041906` The message should read as follows:

    ```python
    "CUSTOMER_ID DEC041906 processed successfully!"
    ```

1. **Update the Tests**:

    Complete the following:

   - Modify `test.py` to replace all instances of `NAME` with `CUSTOMER_ID`.
   - Update test cases to validate the new parameter and success message.

1. **Validate the Changes**:

    Run the `pytest` test suite again to confirm the changes were applied correctly.

This challenge should take 10-15 minutes to complete.

<!-- FooterStart -->
---
[← 03_05 Use a custom pipe in a pipeline](../03_05_use_a_custom_pipe_in_a_pipeline/README.md) | [pytest cache directory # →](../03_07_solution_create_a_custom_pipe/ALPHA-Team-Pipe-SOLUTION/.pytest_cache/README.md)
<!-- FooterEnd -->
