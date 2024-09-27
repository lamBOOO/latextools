from pybtex.database import parse_file

# Load the .bib files
def load_bib(file_path):
    return parse_file(file_path)

# Save the modified .bib file
def save_bib(bib_data, file_path):
    with open(file_path, 'w') as bib_file:
        bib_data.to_file(bib_file)

# Remove extracted entries from the old .bib
def remove_extracted_entries(old_bib, extracted_bib):
    extracted_keys = set(extracted_bib.entries.keys())
    # Remove entries from old_bib that are in extracted_bib
    for key in extracted_keys:
        if key in old_bib.entries:
            del old_bib.entries[key]

# Main function to handle the process
def main(old_bib_file, extracted_bib_file, output_bib_file):
    # Load both bib files
    old_bib = load_bib(old_bib_file)
    extracted_bib = load_bib(extracted_bib_file)

    # Remove extracted references
    remove_extracted_entries(old_bib, extracted_bib)

    # Save the remaining references to a new .bib file
    save_bib(old_bib, output_bib_file)
    print(f"Unused references saved to {output_bib_file}")

# Define paths to .bib files (modify these as necessary)
old_bib_file = "refs_betterbibtex_journalabbrevs.bib"
extracted_bib_file = "extracted.bib"
output_bib_file = "output.bib"

# Run the script
main(old_bib_file, extracted_bib_file, output_bib_file)

