const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

function findYamlFiles(startPath, rootPath = startPath) {
  let results = [];

  function finder(currentPath) {
    const files = fs.readdirSync(currentPath);
    for (let i = 0; i < files.length; i++) {
      const filename = path.join(currentPath, files[i]);
      const stat = fs.lstatSync(filename);
      if (stat.isDirectory()) {
        finder(filename);
      } else if (filename.endsWith('.yml') || filename.endsWith('.yaml')) {
        results.push(path.relative(rootPath, filename)); // Store relative path
      }
    }
  }

  finder(startPath);
  return results;
}

function extractDataAndConvertToCSV(yamlFiles, rootPath) {
  let csvContent = 'Filename,Services.name,Services.url,Services.routes.host,Services.routes.consumer_path\n';

  yamlFiles.forEach(relativeFilePath => {
    try {
      const absoluteFilePath = path.join(rootPath, relativeFilePath); // Construct absolute path
      const fileContent = fs.readFileSync(absoluteFilePath, 'utf8');
      const data = yaml.load(fileContent);

      if (data && data.services && Array.isArray(data.services)) {
        data.services.forEach(service => {
          const name = service.name || '';
          const url = service.url || '';
          const host = service.routes && service.routes.host ? service.routes.host : '';
          const consumerPath = service.routes && service.routes.consumer_path ? service.routes.consumer_path : '';

          csvContent += `${relativeFilePath},"${name}","${url}","${host}","${consumerPath}"\n`; // Use relative path in CSV
        });
      }
    } catch (e) {
      console.error(`Error processing file: ${relativeFilePath}`, e);
    }
  });

  return csvContent;
}

function saveCSVToFile(csvContent, outputFilename = 'extracted_data.csv') {
  fs.writeFileSync(outputFilename, csvContent, 'utf8');
  console.log(`Data extracted and saved to ${outputFilename}`);
}

// Example usage:
const args = process.argv.slice(2); // Remove node and script name from args
let directoryToSearch = './';
let outputFilename = 'extracted_data.csv';

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--path' && args[i + 1]) {
    directoryToSearch = args[i + 1];
    i++; // Skip the next argument (path value)
  } else if (args[i] === '--output' && args[i + 1]) {
    outputFilename = args[i + 1];
    i++; // Skip the next argument (output value)
  }
}

const foundYamlFiles = findYamlFiles(directoryToSearch);

if (foundYamlFiles.length > 0) {
  const csvData = extractDataAndConvertToCSV(foundYamlFiles, directoryToSearch);
  saveCSVToFile(csvData, outputFilename);
} else {
  console.log('No YAML files found to process.');
}