import logging
import os
import yaml

from pathlib import Path

from previsedx_labguru_file_utils.xlsx.parser import Parser
from previsedx_labguru_file_utils import constants

outdir = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.basename(__file__),
    constants.DEFAULT_TIMESTAMP,
)

if not os.path.exists(outdir):
    Path(outdir).mkdir(parents=True, exist_ok=True)


logfile = os.path.join(outdir, f"{os.path.basename(__file__)}.log")
logfile = "my.log"

infile = os.path.join(os.path.dirname(__file__), "examples", "labguru_mockup.xlsx")
config_file = constants.DEFAULT_CONFIG_FILE
config = yaml.safe_load(Path(config_file).read_text())

logging.basicConfig(
    format=constants.DEFAULT_LOGGING_FORMAT,
    level=constants.DEFAULT_LOGGING_LEVEL,
    filename=logfile,
)

parser = Parser(
    config=config,
    config_file=config_file,
    outdir=outdir,
    verbose=True
)

records = parser.get_records(infile)

if len(records) > 0:
    for record in records:
        print(record)
else:
    print("No records found")

print(f"The log file is '{logfile}'")
