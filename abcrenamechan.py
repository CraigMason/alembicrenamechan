#!/usr/bin/env python3

import os, argparse

import cask

msg = "Renames an Ornatrix ABC Almbic channel to an Unreal compatible 'groom_color'"

# Initialize parser
parser = argparse.ArgumentParser(description = msg)

parser.add_argument('-s', '--source_channel', help = "Source channel to rename. Defaults to 'chan_groom_color_RGB'", default = "chan_groom_color_RGB")
parser.add_argument('input_file', help = "Input .abc file")

args = parser.parse_args()

print("Processing {}".format(args.input_file))
print("Renaming channel `{}` to `groom_color`".format(args.source_channel))


def walk(obj):
    print( obj.name, obj.type())
    for child in obj.children.values():
        walk(child)


bakFile = "{}.bak".format(args.input_file)
os.rename(src=args.input_file, dst=bakFile)

# Process the main abc file
a = cask.Archive(bakFile)

# Known structure
geom = a.top.children["GROOMShape"].properties[".geom"]
arbProps = geom.properties['.arbGeomParams']
arbProps.properties[args.source_channel].name = 'groom_color'

a.write_to_file(args.input_file)