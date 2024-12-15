import json
import os


def create_function_config_file(
    function_name, platform, version, build_number, environment, output_path
):
    """
    Creates a JSON file for AWS Lambda function configuration.

    Args:
        function_name (str): Name of the Lambda function.
        platform (str): Platform name to include in the configuration.
        version (str): Version number to include in the configuration.
        build_number (str): Build number to include in the configuration.
        environment (str): Deployment environment (e.g., "production", "staging").
        output_path (str): Path to save the generated JSON file.

    Returns:
        str: Path to the generated JSON file.
    """
    config = {
        "FunctionName": function_name,
        "Environment": {
            "Variables": {
                "PLATFORM": platform,
                "VERSION": version,
                "BUILD_NUMBER": build_number,
                "ENVIRONMENT": environment,
            }
        },
    }

    # Write the configuration to a JSON file
    with open(output_path, "w") as json_file:
        json.dump(config, json_file, indent=4)

    print(f"Configuration file created at: {output_path}")
    return output_path


if __name__ == "__main__":
    FUNCTION_NAME = os.getenv("FUNCTION_NAME", "undefined")
    VERSION = os.getenv("BITBUCKET_COMMIT", "undefined")
    BUILD_NUMBER = os.getenv("BITBUCKET_BUILD_NUMBER", "undefined")
    ENVIRONMENT = os.getenv("BITBUCKET_DEPLOYMENT_ENVIRONMENT", "undefined")
    PLATFORM = os.getenv("PLATFORM", "Bitbucket")
    OUTPUT_PATH = "function_configuration.json"

    create_function_config_file(
        function_name=FUNCTION_NAME,
        platform=PLATFORM,
        version=VERSION,
        build_number=BUILD_NUMBER,
        environment=ENVIRONMENT,
        output_path=OUTPUT_PATH,
    )
