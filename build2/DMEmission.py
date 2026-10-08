# Check to see if the DM Emissions are kinematically valid or not for ALPs with mass of 0.0167 GeV 
# and coupling constant of 0.001 1/GeV

# parses the file taht removed the if condition at DarkMAtter.cc 

import re

filename = "check.txt"

count_below = 0

with open(filename, "r") as f:
    text = f.read()

events = re.split(r'(?=--> Event \d+ starts\.)', text)

for event in events:

    event_match = re.search(r'--> Event (\d+) starts\.', event)

    if not event_match:
        continue

    event_number = int(event_match.group(1))

    energy_match = re.search(
        r'DM energy\s*=\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)',
        event
    )

    if energy_match:
        dm_energy = float(energy_match.group(1))

        if dm_energy < 1:
            count_below += 1
            print(f"Event {event_number}: DM energy = {dm_energy} GeV")

print()
print(f"Number of ALPs with energy below 1 GeV: {count_below}")