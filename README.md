# terraria-backupper

Python script to backup your Terraria worlds.

If you fuck up your world files using this tool, it's your problem.

### Usage

1. Open `conf.conf` and set the `worlds_location` and `backup_localion` directories.

2. Run `python3 backupper.py world-name`

The script will copy your world file to the backup dir and add a version number at the end of the filename. It will also keep a .txt file with every version number and a timestamp of when it was created.

This versioning file uses the following format:

`world-name.ver`
```
# version_number;timestamp
1;2015-11-08 17:00:58.489336
```
