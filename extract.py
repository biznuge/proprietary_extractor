import os
import sys
import yaml
import time

def find_yaml_files(start_path, root_path=None):
    if root_path is None:
        root_path = start_path
    results = []
    for root, _, files in os.walk(start_path):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                results.append(os.path.relpath(os.path.join(root, file), root_path))
    return results

def extract_data_and_convert_to_csv(yaml_files, root_path):
    csv_content = 'Filename,Services.name,Services.url,Services.routes.host,Services.routes.consumer_path\n'
    for relative_file_path in yaml_files:
        print(f"Processing file: {relative_file_path}")
        try:
            absolute_file_path = os.path.join(root_path, relative_file_path)
            with open(absolute_file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)

            if data and 'services' in data and isinstance(data['services'], list):
                for service in data['services']:
                    name = service.get('name', '')
                    url = service.get('url', '').strip()
                    routes = service.get('routes', {})

                    if isinstance(routes, list) and routes:
                        host = routes[0].get('host', '').strip() if isinstance(routes[0], dict) else ''
                        consumer_path = routes[0].get('consumer_path', '').strip() if isinstance(routes[0], dict) else ''
                    elif isinstance(routes, dict):
                        host = routes.get('host', '').strip()
                        consumer_path = routes.get('consumer_path', '').strip()
                    else:
                        host = ''
                        consumer_path = ''

                    csv_content += f'{relative_file_path},"{name}","{url}","{host}","{consumer_path}"\n'

        except Exception as e:
            print(f'Error processing file: {relative_file_path}', e, file=sys.stderr)

    return csv_content

def save_csv_to_file(csv_content, output_filename='extracted_data.csv'):
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(csv_content)
    print(f'Data extracted and saved to {output_filename}')

def main():
    directory_to_search = './'
    output_filename = 'extracted_data.csv'

    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == '--path' and i + 1 < len(args):
            directory_to_search = args[i + 1]
            i += 2
        elif args[i] == '--output' and i + 1 < len(args):
            output_filename = args[i + 1]
            i += 2
        else:
            i += 1

    yaml_files = find_yaml_files(directory_to_search)

    print(f"Total YAML files found: {len(yaml_files)}")

    if yaml_files:
        start_time = time.time()
        csv_data = extract_data_and_convert_to_csv(yaml_files, directory_to_search)
        save_csv_to_file(csv_data, output_filename)
        end_time = time.time()
        print(f"Time taken to create CSV: {end_time - start_time:.2f} seconds")
        print(f"Output file path: {os.path.abspath(output_filename)}")
    else:
        print('No YAML files found to process.')

if __name__ == '__main__':
    main()