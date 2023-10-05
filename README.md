Ornatrix groom_color channel renamer
====================================

Utility image to rename incorrectly exported vertex painted channels to the
expected 'groom_color' that Unreal Engine requires.

See https://docs.unrealengine.com/5.3/en-US/using-alembic-for-grooms-in-unreal-engine/


The Problem
-----------

Since Ornatrix for Maya version 4.0.14, using 'Unreal Export' does not result in
an alembic float32[3] channel called 'groom_color', which is needed to use vertex
painting data within Unreal Engine.

Until this is fixed, this repo / image can be used to rename channels.

Also included in the image are the compiled Alembic utilities for inspecting
alembic files.

Build
-----

```bash
docker build   --tag stasismedia/alembicrenamechan .
```

Usage
-----

To launch the docker container and bind the current dir into it:
```bash
docker run --rm -it -v `pwd`:/app stasismedia/alembicrenamechan
```

To rename a channel:

```bash
abcrenamechan -s chan_groom_color_RGB myfile.abc
```