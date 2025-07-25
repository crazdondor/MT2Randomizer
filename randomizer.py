import argparse
import random
import sys

from pathlib import Path

# Secondary clan pool — customize as you like
CLAN_POOL = [
    "Banished",
    "Pyreborne",
    "Luna Coven",
    "Underlegion",
    "Lazarus League",
    "Hellhorned",
    "Awoken",
    "Stygian Guard",
    "Umbra",
    "Melting Remnant"
]

def handle_randomize_clan(args):
    # Pick a random secondary clan
    # if no clan provided, pick a random primary
    if not args.primary_clan:
        primary_clan = random.choice(CLAN_POOL)
        print(f"Primary clan chosen: {primary_clan}")
    else:
        primary_clan = args.primary_clan

    # select clan pool file
    out_dir = Path("mt2_randomizer_data")
    file = out_dir / f"{primary_clan}_pool.txt"
    with open(file, "r", encoding="utf-8") as f:
        pool = [line.strip() for line in f]
    cleaned = [clan for clan in pool if not clan.endswith("(Done)")]

    if not cleaned:
        print("No valid secondary clans")
        sys.exit(1)
    secondary = random.choice(cleaned)
    print(f"Your combo: {primary_clan} + {secondary}")

def handle_init(args):
    # should create a folder structure at ./clan-combos. one file for each primary clan listing possible secondaries
    out_dir = Path("mt2_randomizer_data")
    out_dir.mkdir(parents=True, exist_ok=True)

    # create each clan file
    for clan in CLAN_POOL:
        out_file = out_dir / f"{clan}_pool.txt"
        out_file_alt = out_dir / f"{clan} Alternate_pool.txt"
        with out_file.open("w", encoding="utf-8") as f:
            pool = [clan2 for clan2 in CLAN_POOL if clan2 != clan]
            for secondary in pool:
                f.write(secondary + "\n")
                f.write(secondary + " - Alternate\n")
        with out_file_alt.open("w", encoding="utf-8") as f:
            pool = [clan2 for clan2 in CLAN_POOL if clan2 != clan]
            for secondary in pool:
                f.write(secondary + "\n")
                f.write(secondary + " Alternate\n")
    
    print(f"Created {len(CLAN_POOL)*2} files for tracking secondary clans")

def handle_mark_done(args):
    primary = args.primary_clan
    secondary = args.secondary_clan

    # select clan pool file
    out_dir = Path("mt2_randomizer_data")
    file = out_dir / f"{primary}_pool.txt"

    edit_file_line(file, secondary, f"{secondary} (Done)")

def edit_file_line(filepath, prefix, replacement):
    path = Path(filepath)
    
    # Read all lines
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    # Modify matching line
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = replacement + "\n"  # ensure newline
            break  # stop after first match (remove if you want all matches)

    # Write the updated lines back
    with path.open("w", encoding="utf-8") as f:
        f.writelines(lines)

def main():
    parser = argparse.ArgumentParser(prog="randomizer", description="Monster Train 2 Clan Randomizer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_files = subparsers.add_parser("init", help="Initialize the MT2 clan tracker files")
    init_files.set_defaults(func=handle_init)

    randomize_parser = subparsers.add_parser("randomize", help="Randomly choose a secondary clan")
    randomize_parser.add_argument(
        "-p", "--primary-clan",
        required=False,
        help="Specify the primary clan"
    )
    randomize_parser.set_defaults(func=handle_randomize_clan)

    mark_done = subparsers.add_parser("mark", help="Mark a clan combo as completed")
    mark_done.add_argument(
        "-p", "--primary-clan",
        required=True,
        help="Specify primary clan in combo"
    )
    mark_done.add_argument(
        "-s", "--secondary-clan",
        required=True,
        help="Specify secondary clan in combo"
    )
    mark_done.set_defaults(func=handle_mark_done)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()