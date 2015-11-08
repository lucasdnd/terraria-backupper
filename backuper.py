import os
import sys
import datetime

# Read the args
if len(sys.argv) != 2:
  print("Usage: python backuper.py world-name")
  print("Example: python backuper.py NewWorld")
  sys.exit()

world_name = str(sys.argv[1])

# Read the settings
worlds_location = ""
backup_location = ""
with open("conf.conf", "r") as conf:
  for line in conf:
    line_split = line.split("=")
    if len(line_split) == 2:
      if line_split[0] == "worlds_location":
        worlds_location = line_split[1].replace("\n", "")
      elif line_split[0] == "backup_location":
        backup_location = line_split[1].replace("\n", "")

# Add a "/" at the end of the paths
if (worlds_location[-1] != "/"):
  worlds_location += "/"
if (backup_location[-1] != "/"):
  backup_location += "/"

# Check if the world file exists
if not os.path.isfile(worlds_location + world_name + ".wld"):
  print("World file not found: " + worlds_location + world_name + ".wld")
  sys.exit()

# Create the versioning file if it doesn't exist
if not os.path.isfile(backup_location + world_name + ".ver"):
  with open(backup_location + world_name + ".ver", "w") as f:
    f.write("# version_number;timestamp")

# Get the next version
next_version = 0
with open(backup_location + world_name + ".ver", "r") as f:

  # Get the last line
  for line in f:
    last_line = line

  # Get the last version
  if "#" in last_line:
    next_version = 1
  else:
    last_version = int(last_line.split(";")[0])
    next_version = last_version + 1

# Backup the world file
with open(backup_location + world_name + ".ver", "a") as f:

  print("Backing up " + world_name + "...")
  os.system("cp " + worlds_location + world_name + ".wld " + backup_location)

  # Version it
  print("Versioning...")
  os.system("mv " + backup_location + world_name + ".wld " + backup_location + world_name + "_" + str(next_version) + ".wld")
  f.write("\n" + str(next_version) + ";" + str(datetime.datetime.now()))
  print("New version: " + str(next_version))

print("Done")
