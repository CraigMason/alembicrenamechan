#!/usr/bin/env python3

import os, argparse

import cask

msg = "Renames an Ornatrix ABC Almbic channel to an Unreal compatible 'groom_color'"

# Initialize parser
parser = argparse.ArgumentParser(description = msg)

parser.add_argument('-g', '--groom_root', help = "Groom name at the root. Defaults to 'GROOMShape'", default = "GROOMShape")
parser.add_argument('-s', '--source_channel', help = "Source channel to rename. Defaults to 'chan_groom_color_RGB'", default = "chan_groom_color_RGB")
parser.add_argument('input_file', help = "Input .abc file")

args = parser.parse_args()

print("Processing {}".format(args.input_file))
print("Renaming channel `{}` to `groom_color`".format(args.source_channel))


def walk(obj):
    print( obj.name, obj.type())
    for child in obj.children.values():
        walk(child)


# Process the main abc file
a = cask.Archive(args.input_file)

# Known structure
geom = a.top.children[args.groom_root].properties[".geom"]
arbProps = geom.properties['.arbGeomParams']
arbProps.properties[args.source_channel].name = 'groom_color'

# Save to a new file
filename, ext = os.path.splitext(args.input_file)
new_filename = f"{filename}_color{ext}"

a.write_to_file(new_filename)