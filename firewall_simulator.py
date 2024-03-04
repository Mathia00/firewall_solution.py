import random

def generate_random_ip():
    """Generate a random IP address."""
    return f"127.0.0.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if no rule matches

def main():
    # Define the firewall rules (key: IP address, value: action)
    firewall_rules = {
        "127.0.0.1": "block",
        "127.0.0.4": "block",
        "127.0.0.9": "block",
        "127.0.0.13": "block",
        "127.0.0.16": "block",
        "127.0.0.19": "block"
    }

      # Simulate network traffic
    for _ in range(12):
     ip_address = generate_random_ip()
     action = check_firewall_rules(ip_address, firewall_rules)
     random_number = random.randint(0, 9999)
     print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()