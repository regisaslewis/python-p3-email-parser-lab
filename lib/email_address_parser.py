import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        pattern = r"[A-z0-9\.]+@[A-z]+\.[a-z]{3,}"
        regex = re.compile(pattern)
        return sorted(set(regex.findall(self.email_addresses)))