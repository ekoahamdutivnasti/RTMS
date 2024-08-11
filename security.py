import hashlib
import uuid
import json
import os

class SecurePasswordGenerator:
    def __init__(self, storage_file='data/generated_passwords.json'):
        self.storage_file = storage_file
        self.generated_passwords = self._load_passwords()

    def _load_passwords(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return set(json.load(file))
        return set()

    def _save_passwords(self):
        with open(self.storage_file, 'w') as file:
            json.dump(list(self.generated_passwords), file)

    def generate_password(self):
        while True:
            random_element = str(uuid.uuid4())
            base = hashlib.sha256(random_element.encode()).hexdigest()
            password = base[:10] + str(uuid.uuid4())[:10]

            if password not in self.generated_passwords:
                self.generated_passwords.add(password)
                self._save_passwords()
                return password
