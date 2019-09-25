import re
from collections import defaultdict


def get_entry(config, entry_lines):
    entry = config.copy()
    lines = [line[2:].strip() for line in entry_lines]
    entry['lines'] = lines

    text = ' '.join(lines)
    pr_match = re.search(r'\[ ([^]]+) \] [\.\s]* $', text, re.VERBOSE)
    if pr_match:
        entry['pr_number'] = pr_match.group(1)

    return entry


def parse_changes_rst():
    with open('CHANGES_test.rst') as fh:
        lines = fh.readlines()
    lines.append('')

    config = {}
    entry_lines = []
    entries = []
    within_entry = False

    for line, line_next in zip(lines, lines[1:]):
        if within_entry or line.startswith('- '):
            entry_lines.append(line)

            if line_next.startswith('  '):
                within_entry = True
            else:
                within_entry = False
                entries.append(get_entry(config, entry_lines))
                entry_lines.clear()

        elif re.match(r'[\^]+\s*$', line_next):
            config['subpackage'] = line.strip()

        elif re.match(r'[=]+\s*$', line_next):
            config['release'] = line.strip()
            config['subpackage'] = None
            config['entry_type'] = None

        elif re.match(r'[-]+\s*$', line_next):
            config['entry_type'] = line.strip()
            config['subpackage'] = None

    return entries


if __name__ == '__main__':
    entries = parse_changes_rst()

    uniques = defaultdict(set)
    for entry in entries:
        for key in ('subpackage', 'release', 'entry_type', 'pr_number'):
            uniques[key].add(entry.get(key))
