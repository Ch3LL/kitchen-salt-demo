import os
import pytest
import subprocess
import testinfra

@pytest.fixture()
def host():
  return testinfra.get_host('docker://{KITCHEN_USERNAME}@{KITCHEN_CONTAINER_ID}'.format(**os.environ))

@pytest.fixture()
def port():
    ret = subprocess.check_output(
          ['docker', 'port', os.environ.get('KITCHEN_CONTAINER_ID'), "80/tcp"]
    ).decode().split(':')[-1].strip('\n')
    return ret

@pytest.fixture()
def url(port):
    return f'http://localhost:{port}'
