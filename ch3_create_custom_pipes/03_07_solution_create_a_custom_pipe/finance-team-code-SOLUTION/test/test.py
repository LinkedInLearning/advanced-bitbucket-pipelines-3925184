import os
import subprocess

docker_image = 'bitbucketpipelines/demo-pipe-python:ci' + os.getenv('BITBUCKET_BUILD_NUMBER', 'local')

def docker_build():
  """
  Build the docker image for tests.
  :return:
  """
  args = [
    'docker',
    'build',
    '-t',
    docker_image,
    '.',
  ]
  subprocess.run(args, check=True)


def setup():
  docker_build()

def test_no_parameters():
  args = [
    'docker',
    'run',
    docker_image,
  ]

  result = subprocess.run(args, check=False, text=True, capture_output=True)
  assert result.returncode == 1
  assert '✖ Validation errors: \nCUSTOMER_ID:\n- required field' in result.stdout

def test_success():
  args = [
    'docker',
    'run',
    '-e', 'CUSTOMER_ID=1234567890',
    docker_image,
  ]

  result = subprocess.run(args, check=False, text=True, capture_output=True)
  assert '1234567890' in result.stdout
  assert result.returncode == 0

