import unittest
import subprocess
import json
from pathlib import Path

class TestScript(unittest.TestCase):
    def setUp(self):
        self.config_path = 'test_config.json'
        sample_config = {
            "server": "my-server.com",
            "server_port": 8388,
            "password": "mypassword",
            "method": "aes-256-gcm",
            "remarks": "Test Server"
        }
        with open(self.config_path, 'w') as f:
            json.dump(sample_config, f)

    def tearDown(self):
        if Path(self.config_path).exists():
            Path(self.config_path).unlink()

    def test_generate_uri(self):
        result = subprocess.run(
            ['python3', 'ss-genuri.py', '--config', self.config_path],
            capture_output=True,
            text=True
        )
        self.assertEqual('ss://YWVzLTI1Ni1nY206bXlwYXNzd29yZEBteS1zZXJ2ZXIuY29tOjgzODg=#TestServer\n', result.stdout)

if __name__ == '__main__':
    unittest.main()

