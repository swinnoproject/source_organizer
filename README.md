# Source Organizer

When working with sources in SWINNO, it can be helpful to sort them according to their SINNO ID.
This script creates a folder for each SINNO ID provided as input with all sources associated with that ID.
By default, source articles are not copied, but a symlink is created in the folder pointing to the source on OneDrive.

## Usage
1. Create a txt file of SINNO IDs, with one ID per line in the txt file
2. run scripts/find_sources with .txt of sinno_ids as input 
