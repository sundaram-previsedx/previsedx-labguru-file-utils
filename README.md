# previsedx-labguru-file-utils

Software for processing Labguru-derived files.

- [previsedx-labguru-file-utils](#previsedx-labguru-file-utils)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Class Diagrams](#class-diagrams)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)


## Improvements

Please see the [TODO](docs/TODO.md) for a list of upcoming improvements.

## Use Cases

<img src="use_cases.png" width="400" height="200" alt="Use Case diagram">

## Class Diagrams

![class diagrams](class_diagrams.png)

## Installation

Please see the [INSTALL](docs/INSTALL.md) guide for instructions.

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
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](docs/TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](docs/CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](docs/LICENSE)
