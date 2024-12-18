# 03_07 Solution: Develop a custom pipe

## Challenge Scenario

The world-renowned Amazing Mobile App is expanding!  Their new strategy will allow business partners to integrate with the mobile app directly from their deployment pipelines using APIs.

The initiative is led by the Amazing Library for Phone Hooks and APIs (ALPHA) Team. The ALPHA Team is planning to base the new integration on credentials that include an API key and a Customer ID.

Before implementing the API interface, the ALPHA team is asking you to a demonstrate how customers can use a pipe to call the ALPHA API. They've asked you to update their code (which was generated using a Python-based Complete Pipe template) to use the `CUSTOMER_ID` parameter instead of the `NAME` parameter.

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

## Solution

For reference, you can find the code that implements the solution in the exercise files for this lesson.

- [pipe/pipe.py](./ALPHA-Team-Pipe-SOLUTION/pipe/pipe.py)
- [test/test.py](./ALPHA-Team-Pipe-SOLUTION/test/test.py)

1. **Run the Test Suite**:

    ```bash
    pytest --verbose test/test*.py
    ```

    Output should be similar to:

    ```bash
    ===== test session starts =====
    ...
    collected 2 items

    test/test.py::test_no_parameters PASSED [ 50%]
    test/test.py::test_success PASSED       [100%]

    ===== 2 passed in 1.94s =====
    ```

1. **Explore the Provided Code**:

    Because we know that the string `NAME` is the target for this change, a quick way to explore the files before editing is to use the `find` command:

    ```bash
    find . -type f -name \*.py -exec grep -n NAME {} \;
    ```

1. **Update the Code**:

    1. Edit the script `pipe/pipe.py`.

    1. Update the schema:

        ```python
        'NAME': {'type': 'string', 'required': True}
        ```

        Becomes...

        ```python
        'CUSTOMER_ID': {'type': 'string', 'required': True}
        ```

    1. Update the `self.get_variable()` call:

        ```python
        name = self.get_variable('NAME')
        ```

        Becomes...

        ```python
        customer_id = self.get_variable('CUSTOMER_ID')
        ```

    1. Update the `self.success()` message:

        ```python
        self.success(message="Success!")
        ```

        Becomes...

        ```python
        self.success(message=f"CUSTOMER_ID {customer_id} processed successfully!")
        ```

1. **Update the Tests**:[^1]

    1. Edit the script `test/test.py`.

    1. Update the `test_no_parameters()` function:

        ```python
        assert '✖ Validation errors: \nNAME:\n- required field' in result.stdout
        ```

        Becomes...

        ```python
        assert '✖ Validation errors: \nCUSTOMER_ID:\n- required field' in result.stdout        ```

    1. Update the `test_success()` function:

        ```python
        '-e', 'NAME=hello world',
        ```

        Becomes...

        ```python
        '-e', 'CUSTOMER_ID=DEC041906',
        ```

        and

        ```python
        assert 'hello world' in result.stdout
        ```

        Becomes...

        ```python
        assert 'DEC041906' in result.stdout
        ```

1. **Validate the Changes**:

    Run the `pytest` command again.  The tests should be passing.  If tests fail, review your changes and make updates as needed until you get the test passing.

## Reference Code


[^1]: Maybe its just me but I like to run the test suite again after making changes like this to eliminate any false sense of security.  If I make changes and the test suite passes, is the test suite really working?  In this case I would expect both tests to fail after the code was updated.

<!-- FooterStart -->
---
[← pytest cache directory #](ALPHA-Team-Pipe-SOLUTION/.pytest_cache/README.md) | [04_01 When to Use Self-Hosted Runners →](../../ch4_self_hosted_runners/04_01_when_to_use_self_hosted_runners/README.md)
<!-- FooterEnd -->
