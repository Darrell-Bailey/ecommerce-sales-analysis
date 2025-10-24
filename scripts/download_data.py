import os
import subprocess

# Run Kaggle download via subprocess (assumes API setup)
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)
subprocess.run([
	"kaggle", "datasets", "download", "-d", "olistbr/brazilian-ecommerce",
    	"-p", output_dir, "--unzip"
], check=True)
print("Dataset downloaded and unzipped to data/")
