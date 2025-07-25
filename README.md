# MT2Randomizer

A simple CLI tool for choosing random clan combinations in Monster Train 2  
I made this because I prefer playing with random clan combos, but I still want to work towards completion of all combos. This allows for picking out of a select pool, and marking combos as done

## Usage

Requires python3  
Run init command first or the tracking and randomizing won't work  
All arguments should be wrapped in quotes  
If confused about what each clan should look like, just copy from each file

### Init
Creates files for tracking all possible clan combinations
#### Example
python .\randomizer.py init

### Randomize
Randomizes based on specified primary clan or full random
#### Examples
python .\randomizer.py randomize -p "Lazarus League"  
python .\randomizer.py randomize
#### Arguments
##### --primary-clan OR -p
Not required. Specifies primary clan

### Mark
Marks a clan combination as done. Excludes it from randomization
#### Example
python .\randomizer.py mark -p "Pyreborne" -s "Luna Coven Alternate"
#### Arguments
##### --primary-clan OR -p
Required. Specifies primary clan
##### --secondary-clan OR -s
Required. Specifies secondary clan
