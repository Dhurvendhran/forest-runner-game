import json
import os
import re
import sys

# Define the version pattern to search for
version_pattern = re.compile(r'v(\d+)')

# Get the input file path from the command-line arguments
if len(sys.argv) < 2:
    print("Error: No input file path provided.")
    sys.exit(1)

input_file_path = sys.argv[1]

# Extract the version from the file path
match = version_pattern.search(input_file_path)
if not match:
    print("Error: Invalid input file path format.")
    sys.exit(1)

current_version = match.group(1)
new_version = str(int(current_version) + 1)

# Generate the new file name based on the input file path
filename = os.path.basename(input_file_path)
output_file = filename.replace(f'v{current_version}', f'v{new_version}')

# Read the input JSON file
if not os.path.exists(input_file_path):
    print(f"Error: Input file {input_file_path} does not exist.")
    sys.exit(1)

with open(input_file_path, 'r') as file:
    data = json.load(file)

# Update the version in the metadata
data['metadata']['version'] = f'v{new_version}'

# Update the $id field if it exists
if "$id" in data:
    data["$id"] = data["$id"].replace(f'v{current_version}', f'v{new_version}')

# Update the schema version to 0.4.0
if "schema" in data:
    data["schema"] = "0.4.0"

# Update the $schema field if it exists
if "$schema" in data:
    data["$schema"] = data["$schema"].replace("0.2.0", "0.4.0")

# Update the data_topic field if it exists
if "data_topic" in data:
    if "topic_id" in data["data_topic"]:
        data["data_topic"] = {"topic_id": [data["data_topic"]["topic_id"]]}  # Retain only topic_id as a list

# Add backport field if it doesn't exist
if "backport" not in data:
    dar_uri = os.path.dirname(input_file_path)  # Extract base URI from input file path
    data["backport"] = [
        {
            "dar_uri": f"{dar_uri}/v{new_version}",  # Ensure the version is appended
            "transform_ref": "identifier",
            "enabled": True
        }
    ]

# Save the updated JSON to the new file
output_file_path = os.path.join(os.path.dirname(input_file_path), output_file)
with open(output_file_path, 'w') as file:  # Save in the same directory as the input file
    json.dump(data, file, indent=4)

print(f"Updated version from v{current_version} to v{new_version}, schema to 0.4.0, and saved to {output_file_path}.")
