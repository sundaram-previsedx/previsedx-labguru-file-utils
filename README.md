# previsedx-labguru-file-utils

Software for processing Labguru-derived files.

- [previsedx-labguru-file-utils](#previsedx-labguru-file-utils)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Use Cases](#use-cases-1)
  - [Class Diagrams](#class-diagrams)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Exported scripts](#exported-scripts)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)


## Improvements

Please see the [TODO](docs/TODO.md) for a list of upcoming improvements.


## Use Cases

<img src="use_cases.png" width="400" height="400" alt="Use Cases diagram">

## Use Cases

<img src="use_cases.png" width="400" height="400" alt="Use Cases diagram">

## Class Diagrams

![class diagrams](class_diagrams.png)

## Installation

Please see the [INSTALL](docs/INSTALL.md) guide for instructions.

## Usage

```python
from previsedx_labguru_file_utils import Manager

config_file = "conf/config.yaml"
config = yaml.safe_load(Path(config_file).read_text())

manager = Manager(
    config=config,
    config_file=config_file,
    logfile=logfile,
    outdir=outdir,
    outfile=outfile,
    verbose=verbose,
)

infile = "labguru.xlsx"
records = manager.get_records(infile)

```

## Exported scripts

To use the exported script for ... :

```bash

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
