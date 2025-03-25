# YAML to CSV Extractor

This script extracts specific fields from YAML files (`.yml` or `.yaml`) within a given directory structure and outputs them into a CSV file.

This is to extract data from a proprietary .yml format to a CSV format for data engineering purposes.

## Fields Captured

The script captures the following fields from each service definition within the YAML files:

* **Filename:** The relative path of the YAML file from the root directory.
* **Services.name:** The name of the service.
* **Services.url:** The URL of the service.
* **Services.routes.host:** The host specified in the service's routes.
* **Services.routes.consumer_path:** The consumer path specified in the service's routes.

## Low Dependency Installation

This script has only one external dependency:

* **`js-yaml`:** A YAML parser for Node.js.

To install it, run the following command in your project directory:

```
npm install js-yaml
```

## Usage
Save the script: Save the provided Node.js script (e.g., as extract_yaml_data.js).

Run the script: Open your terminal or command prompt, navigate to the directory where you saved the script, and run it using Node.js:

```
node extract_yaml_data.js [directory_path]
```

Replace [directory_path] with the path to the directory containing your YAML files.

If you omit [directory_path], the script will search the current directory and its subdirectories.

## Example Usage of --path flag

Search in a relative directory named config:

```node extract_yaml_data.js --path config```

Search in an absolute directory:

```node extract_yaml_data.js --path  /home/user/my_configs```

Search in the current directory and its subdirectories:

```node extract_yaml_data.js```

or

```node extract_yaml_data.js --path  . ```

## Example Usage of --output flag

> Note: Only filename can be changed, not path.

Change the name of the output file like so

```node extract_yaml_data.js --output my-extract.csv```

Or to default to 'extracted_data.csv' omit the flag

```node extract_yaml_data.js```

## Output

The script will generate a CSV file named extracted_data.csv in the same directory as the script. This file will contain the extracted data in the specified format.

## Pull, Install, and Run (Node.js 20)

These instructions assume you have Node.js version 20 installed, however the script may work (untested as yet) on versions above and below this.

### Clone the Repository:

If you have a Git repository for this script, clone it to your local machine:

```
git clone <repository_url>
cd <repository_name>
Replace <repository_url> with the URL of your repository and <repository_name> with the name of the cloned directory.
```

### Install Dependencies:

Navigate to the project directory in your terminal.

Install the js-yaml dependency using npm:

```
npm install
```

This will install all dependencies listed in the package.json file (if you have one) or just js-yaml if that is the only dependency.

### Run the Script with test data:

Execute the extract_yaml_data.js script, providing the directory path as an argument:

```
node extract.js --path ./config_folder
```

To run this script with your own content, point this script at it using the --path flag.
