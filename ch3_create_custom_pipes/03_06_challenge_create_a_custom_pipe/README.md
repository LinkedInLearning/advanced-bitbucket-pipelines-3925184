# 03_06 Challenge: Develop a custom pipe [text]

## Challenge Scenario

The Amazing Mobile App finance team is working on a CI/CD pipeline that requires an enhanced pipe for generating reports in JSON. As the resident Bitbucket Pipelines expert, you've been asked to demonstrate how they can add functionality to code generated using with the "Advanced Python" pipe template.

Using the code provided in the exercise files for this lesson, make the changes requested and confirm all the tests pass.

## Challenge Tasks

> [!IMPORTANT]
> Review the notes in [03_02 Develop a Custom Pipe](../03_02_develop_a_custom_pipe/README.md) for details on the tools you'll need to have installed

1. **Implement New Functionality:**

   - Add a new function to `pipe/pipe.py` that generates a JSON summary.
   - Modify the existing script to call the function and print the value returned.
   - Use the following code:

        ```python
        import json

        def generate_summary(params):
            # Convert parameters to a JSON string
            return json.dumps(params, indent=2)
        ```

2. **Update Tests:**

   - Add test cases to `test/test.py` to validate the new functionality.
   - Ensure the tests confirm the correctness of the JSON summary format and content.

       *Example test case:*

        ```python
        def test_generate_summary():
            test_values = { "dataset": "dataset.csv", "model": "model.pkl", "summary": "summary.txt" }
            test_result = generate_summary(test_values)
            assert '"dataset": "dataset.csv"' in test_result
            assert '"model": "model.pkl"' in test_result
            assert '"summary": "summary.txt"' in test_result
        ```

3. **Run and Validate Tests:**

   - Use `pytest` to run the tests in the `test/` directory.

        ```bash
        pytest --verbose test/test*.py
        ```

   - Confirm all tests pass.

<!-- FooterStart -->
---
[← 03_05 Use a custom pipe in a pipeline](../03_05_use_a_custom_pipe_in_a_pipeline/README.md) | [03_07 Solution: Develop a custom pipe →](../03_07_solution_create_a_custom_pipe/README.md)
<!-- FooterEnd -->
