import unittest
import subprocess
import json
from pathlib import Path

class TestScript(unittest.TestCase):
    def setUp(self):
        self.config_path = 'test_config.json'
        sample_config = {
            "remarks": "ShadowSocks Server",
            "server":"github.com",
            "server_port":8388,
            "password":"fake_pwd",
            "method":"chacha20-ietf-poly1305"
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
        self.assertEqual('ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmYWtlX3B3ZEBnaXRodWIuY29tOjgzODg=#ShadowSocks%20Server\n', result.stdout)

if __name__ == '__main__':
    unittest.main()
