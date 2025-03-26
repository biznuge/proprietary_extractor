# YAML to CSV Extractor

This script extracts specific fields from YAML files (`.yml` or `.yaml`) within a given directory structure and outputs them into a CSV file.

## Fields Captured

The script captures the following fields from each service definition within the YAML files:

* **Filename:** The relative path of the YAML file from the root directory.
* **Services.name:** The name of the service.
* **Services.url:** The URL of the service.
* **Services.routes.host:** The host specified in the service's routes.
* **Services.routes.consumer_path:** The consumer path specified in the service's routes.

## Dependencies

* **PyYAML:** A YAML parser for Python.

## Installation

1.  **Clone the Repository:**
    * If you have a Git repository for this script, clone it to your local machine:

        ```bash
        git clone <repository_url>
        cd <repository_name>
        ```

        Replace `<repository_url>` with the URL of your repository and `<repository_name>` with the name of the cloned directory.

2.  **Install Dependencies:**
    * Navigate to the project directory in your terminal.
    * Install the required Python packages using `pip`:

        ```bash
        pip install -r requirements.txt
        ```

        This will install `pyyaml` (and any other dependencies listed in `requirements.txt`).

## Usage

1.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the script, and run it using Python 3:

    ```bash
    python3 extract.py --path [directory_path] --output [output_filename]
    ```

    > NOTE: JOHN - DO NOT USE TILDE '~' - Relative or absolute paths only. ;)

    * Replace `[directory_path]` with the path to the directory containing your YAML files.
    * Replace `[output_filename]` with the desired output filename.
    * If you omit `--path`, the script will search the current directory and its subdirectories.
    * If you omit `--output`, the output file will be named `extracted_data.csv`.

## Example Usage

* **Search in a relative directory named `config` and use the default output filename:**

    ```bash
    python3 extract.py --path config
    ```

* **Search in an absolute directory and specify a custom output filename:**

    ```bash
    python3 extract.py --path /home/user/my_configs --output my_output.csv
    ```

* **Search in the current directory and use a custom output filename:**

    ```bash
    python3 extract.py --output results.csv
    ```

* **Search in the current directory and use the default output filename:**

    ```bash
    python3 extract.py
    ```

## Output

The script will generate a CSV file with the specified name in the same directory as the script. This file will contain the extracted data in the specified format.