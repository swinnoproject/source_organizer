import argparse
from pathlib import Path
from source_organizer.utils import get_project_root
from source_organizer.file_utils import (
    create_directory,
    get_input_ids,
    get_source_names,
    copy_files,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", "--input", required=True, help="Text file containing input ids."
)

parser.add_argument(
    "-l",
    "--lookup",
    required=False,
    type=Path,
    default="assets/innovation_id_to_source_id.txt",
    help="Text file containing id lookup pairs.",
)

parser.add_argument(
    "-s",
    "--source",
    type=Path,
    help="Path for source of files.",
)

parser.add_argument(
    "-d",
    "--destination",
    required=False,
    type=Path,
    help="Destination path in which to create destination dir",
)

args = vars((parser.parse_args()))


if __name__ == "__main__":
    if not Path(args["input"]).exists():
        raise FileNotFoundError(f"Input file {args['input']} does not exist.")
    else:
        input_path = Path(args["input"])

    if not Path(args["lookup"]).exists():
        raise FileNotFoundError(f"Lookup file {args['lookup']} does not exist.")
    else:
        lookup_path = Path(args["lookup"])
    if not Path(args["source"]).exists():
        source_path = Path(args["source"])
        raise NotADirectoryError(f"The directory '{source_path.name}' does not exist.")
    else:
        source_path = args["source"]

    destination_path = Path(args["destination"])
    create_directory(destination_path)

    input_ids = get_input_ids(input_path)
    source_names = get_source_names(lookup_path, input_ids)

    copy_files(source_names, source_path, destination_path)
