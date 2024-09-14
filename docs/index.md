# Welcome to PreviseDx Labguru File Utils

Collection of Python modules for processing Labguru Excel .xlsx files.

## Usage


```python
from previsedx_labguru_file_utils import constants
from previsedx_labguru_file_utils import LabguruXlsxParser

# You can override any of the following by providing your own configuration file:
# - the sheet name
# - expected column headers
# - the Excel library (default is openpyxl)
config_file = "conf/config.yaml"
if not os.path.exists(config_file):
  config_file = constants.DEFAULT_CONFIG_FILE
config = yaml.safe_load(Path(config_file).read_text())

parser = Parser(
    config=config,
    config_file=config_file,
    logfile=logfile,
    outdir=outdir,
    outfile=outfile,
    verbose=verbose,
)

infile = "labguru.xlsx"
records = parser.get_records(infile)
```

## References

[GitHub](https://github.com/sundaram-previsedx/previsedx-labguru-file-utils)
[PYPI](https://pypi.org/project/previsedx-labguru-file-utils/)
