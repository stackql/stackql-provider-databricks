#!/usr/bin/env node

import { docgen } from '@stackql/provider-utils';

async function generateDocs() {
  // Get command line arguments
  const args = process.argv.slice(2);
  const getArg = (flag) => {
    const index = args.indexOf(flag);
    return index !== -1 ? args[index + 1] : null;
  };

  const providerName = getArg('--provider-name');
  const providerDir = getArg('--provider-dir');
  const outputDir = getArg('--output-dir');
  const providerDataDir = getArg('--provider-data-dir');
  const dereferenced = getArg('--dereferenced') === 'true';

  if (!providerName || !providerDir || !outputDir || !providerDataDir) {
    console.error('Error: Missing required arguments');
    console.error('Usage: node generate-docs.mjs --provider-name NAME --provider-dir DIR --output-dir DIR --provider-data-dir DIR [--dereferenced true|false]');
    process.exit(1);
  }

  try {
    console.log(`Generating docs for provider: ${providerName}`);
    console.log(`Provider directory: ${providerDir}`);
    console.log(`Output directory: ${outputDir}`);
    console.log(`Provider data directory: ${providerDataDir}`);
    console.log(`Using dereferenced API: ${dereferenced}`);

    const result = await docgen.generateDocs({
      providerName,
      providerDir,
      outputDir,
      providerDataDir,
      dereferenced
    });
    
    console.log('Documentation generated successfully:', result);
  } catch (error) {
    console.error('Error generating documentation:', error);
    process.exit(1);
  }
}

generateDocs();