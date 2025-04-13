import re


input_file = "uBlock_filters.txt"
output_file = "sorted_uBlock_filters.txt"
sites_filtered = {}


def extract_site_from_line(line):
    """Extract the site from a line that starts with ’!’"""

    match_site = re.search(r"https?://\S+", line)
    if match_site:
        return match_site.group(0)
    return None


def clean_data(lines):
    """Gather the filters by site and
    exclude blank lines and the duplication filters"""

    current_site = None

    for line in lines:
        line = line.strip("\n")

        if line.startswith("!"):
            current_site = extract_site_from_line(line)

            if current_site not in sites_filtered:
                sites_filtered[current_site] = set()

        elif current_site and line:
            sites_filtered[current_site].add(line)


def sorted_filters_in_site():
    """Sort filters alphabetically within each site"""

    for key_site in sites_filtered:
        sites_filtered[key_site] = sorted(sites_filtered[key_site])


def write_clean():
    """Write cleaned data to the output file"""

    with open(output_file, 'w') as f:

        for site in sorted(sites_filtered):
            f.write(f"! {site}\n")

            for filter in sites_filtered[site]:
                f.write(f"{filter}\n")

            f.write("\n")


def main():

    with open(input_file, 'r') as f:
        lines = f.readlines()

    clean_data(lines)
    sorted_filters_in_site()
    write_clean()


main()
