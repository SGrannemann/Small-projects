# Small script that copies files in one directory to another
# using glob patterns to specify the files to be copied.

import shutil
from pathlib import Path


inputPath = Path('/home/soeren/Documents/NLTKCorpusTest/')

outputPath = Path.cwd() / Path('Output')
if not outputPath.exists():
    outputPath.mkdir()
for file in inputPath.glob('Stanford*'):
    shutil.copy(file, outputPath)
