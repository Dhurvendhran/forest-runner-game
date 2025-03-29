import json

# Load the JSON file
with open('org_v1.json', 'r') as file:
    data = json.load(file)

# Modify the metadata
data['metadata'] = data.get('metadata', {})  # Ensure metadata exists
data['metadata']['key'] = 'new_value'  # Update or add a key-value pair

# Save the modified JSON as org_v2.json
with open('org_v2.json', 'w') as file:
    json.dump(data, file, indent=4)