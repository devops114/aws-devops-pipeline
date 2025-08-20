
import logging
import random
from datetime import datetime, timedelta

# Configure the log file
log_file = "devops_synthetic.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Simulate different log messages for a DevOps pipeline
log_templates = {
    "INFO": [
        "Build started for commit ID: {commit_id}",
        "Build stage completed successfully in {duration}ms",
        "Testing phase passed. No errors found.",
        "Artifact published successfully.",
        "Deployment to staging environment started."
    ],
    "WARNING": [
        "Build took longer than expected: {duration}ms",
        "Disk usage above 80% on agent server",
        "Node version mismatch. Using fallback."
    ],
    "ERROR": [
        "Build failed due to compilation errors in {file}",
        "Test suite failed: {test_name}",
        "Deployment failed: Connection timeout to server {server_ip}",
        "Container deployment error: Image {image_name} not found"
    ]
}

# Generate a random commit ID
def generate_commit_id():
    return ''.join(random.choices('0123456789abcdef', k=8))

# Generate a series of log entries
def generate_logs(num_entries=1000):
    start_time = datetime.now() - timedelta(days=1) # Start from 1 day ago
    
    for i in range(num_entries):
        # 80% INFO, 10% WARNING, 10% ERROR
        level = random.choices(
            ["INFO", "WARNING", "ERROR"],
            weights=[0.8, 0.1, 0.1],
            k=1
        )[0]
        
        # Pick a random message template for the chosen level
        message_template = random.choice(log_templates[level])
        
        # Fill in the template variables
        log_message = message_template.format(
            commit_id=generate_commit_id(),
            duration=random.randint(100, 5000),
            file=f"src/app_{random.randint(1, 5)}.py",
            test_name=f"test_feature_{random.randint(1, 10)}",
            server_ip=f"192.168.1.{random.randint(1, 50)}",
            image_name=f"app_image:v{random.randint(1, 3)}.{random.randint(0, 5)}"
        )
        
        # Log the message
        logging.log(getattr(logging, level), log_message)

# Generate 1000 log entries
generate_logs(1000)
print(f"Generated 1000 synthetic log entries in {log_file}")
