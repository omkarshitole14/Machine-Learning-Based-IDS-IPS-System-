import random

ATTACKS = [
    "Web Browsing",
    "FTP Download",
    "Email Traffic",
    "SSH Login",
    "Port Scan",
    "DoS Attack",
    "SQL Injection",
    "XSS Attack"
]

def generate_traffic():

    attack_type = random.choice(ATTACKS)

    traffic = {
        "duration": random.randint(0, 1000),
        "protocol_type": random.randint(0, 2),
        "service": random.randint(0, 50),
        "flag": random.randint(0, 10),
        "src_bytes": random.randint(0, 50000),
        "dst_bytes": random.randint(0, 50000),
        "land": random.randint(0, 1),
        "wrong_fragment": random.randint(0, 5),
        "urgent": random.randint(0, 3),
        "hot": random.randint(0, 20),
        "num_failed_logins": random.randint(0, 10),
        "logged_in": random.randint(0, 1),
        "num_compromised": random.randint(0, 20),
        "root_shell": random.randint(0, 1),
        "su_attempted": random.randint(0, 1),
        "num_root": random.randint(0, 10),
        "num_file_creations": random.randint(0, 10),
        "num_shells": random.randint(0, 5),
        "num_access_files": random.randint(0, 10),
        "num_outbound_cmds": 0,
        "is_host_login": random.randint(0, 1),
        "is_guest_login": random.randint(0, 1),
        "count": random.randint(0, 500),
        "srv_count": random.randint(0, 500),
        "serror_rate": random.random(),
        "srv_serror_rate": random.random(),
        "rerror_rate": random.random(),
        "srv_rerror_rate": random.random(),
        "same_srv_rate": random.random(),
        "diff_srv_rate": random.random(),
        "srv_diff_host_rate": random.random(),
        "dst_host_count": random.randint(0, 255),
        "dst_host_srv_count": random.randint(0, 255),
        "dst_host_same_srv_rate": random.random(),
        "dst_host_diff_srv_rate": random.random(),
        "dst_host_same_src_port_rate": random.random(),
        "dst_host_srv_diff_host_rate": random.random(),
        "dst_host_serror_rate": random.random(),
        "dst_host_srv_serror_rate": random.random(),
        "dst_host_rerror_rate": random.random(),
        "dst_host_srv_rerror_rate": random.random()
    }

    return traffic, attack_type