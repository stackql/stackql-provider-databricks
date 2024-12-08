#!/usr/bin/env python3
import yaml
import argparse
import subprocess
import sys

def process_manifest(provider):
    """Process the API manifest file based on provider type."""
    # Determine which manifest file to read
    manifest_file = f"{provider}_api_manifest.yml"
    
    try:
        with open(manifest_file, 'r') as f:
            manifest = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {manifest_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing {manifest_file}: {e}")
        sys.exit(1)

    # Process each service in the manifest
    for service_name, service_data in manifest['services'].items():
        for resource in service_data['resources']:
            resource_name = resource['name']
            for method in resource['methods']:
                # Call dummy.py with the required arguments
                subprocess.run([
                    'python3',
                    'get-api-data.py',
                    '--provider', provider,
                    '--service', service_name,
                    '--resource', resource_name,
                    '--method', method['name'],
                    '--docPath', method['docPath'],
                    '--verb', method['verb']
                ])

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process Databricks API documentation')
    parser.add_argument('provider', choices=['account', 'workspace'],
                      help='The provider type to process (account or workspace)')

    # Parse arguments
    args = parser.parse_args()

    # Process the manifest for the specified provider
    process_manifest(args.provider)

if __name__ == "__main__":
    main()