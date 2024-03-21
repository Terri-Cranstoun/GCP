from google.cloud import storage
import json

# Replace 'your-project-id' with your Google Cloud project ID
project_id = 'your-project-id'

# Initialize Google Cloud Storage client
storage_client = storage.Client(project=project_id)

# Name of the destination bucket to be created
destination_bucket_name = 'your-bucket-name'

# Load JSON file containing attachment filenames
json_file_path = 'your-file.json'

# Read JSON file line by line and upload URLs to storage bucket
with open(json_file_path, 'r') as file:
    for line in file:
        try:
            entry = json.loads(line)
            url = entry["content"]["uri"]
            # Create a destination blob object (even if empty initially)
            destination_blob = storage_client.bucket(destination_bucket_name).blob(url)

            # Upload the URL to GCS as a string object
            destination_blob.upload_from_string(url.encode('utf-8'), content_type='text/plain')
            print(f'Uploaded URL {url} to GCS bucket {destination_bucket_name}')
        except KeyError:
            print("URI not found in entry")
        except Exception as e:
            print(f"Error uploading URL: {str(e)}")
