# writeusb

A Python script to write SAM Coupé disk images to a USB floppy drive so they can
be used on real SAM hardware.

Source disk images should be normal 80/2/10/512 format and in MGT/SAD/EDSK disk
image containers. SAMDOS/MasterDOS/BDOS and some custom loaders are supported.

## Background

USB floppy drives are usually limited to 1.44M (18-sector) and 720K (9-sector)
formats used by PC floppy disks. This is a problem for regular SAM disks, which
use a 10-sector disk format.

This script re-maps the sectors used by the files on the source disk image so it
uses only 9 sectors on each track. It also patches the boot loaders on converted
disks to keep within these limits. Most SAM disks should support conversion.

Please note that this script will NOT help to read existing 10-sector SAM Coupé
disks. The 10th sector on each track is inaccessible on USB floppy drives.

## Requirements

- Windows, Linux or macOS
- USB floppy drive and double-density disks
- [Python 3.6](https://www.python.org/downloads/) (or later)

## Installation

To install:
```
python -m pip install mgtwriteusb
```

Or to install from local source code:
```
python setup.py install
```

To upgrade to the latest version:
```
python -m pip install --upgrade mgtwriteusb
```

## Command-line Options

```
usage: writeusb [-h] [-o OUTPUT] [-p] [-n] [-f] [-a] [-s] diskimage

Write SAM disk image to USB floppy drive

positional arguments:
  diskimage

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output to disk image file
  -p, --pad             pad output disk image to 10 sectors
  -n, --noverify        don't verify disk after writing
  -f, --force           write even if boot loader is unknown
  -a, --all             write all tracks, not just used tracks
  -s, --sniff           detect boot loader on source image
```

## Examples

Convert `image.dsk` to 9-sector format, write used tracks to the connected USB
floppy drive, then verify the written data:

```
writeusb image.dsk
```

Convert `image.dsk` to 9-sector format, save output to disk image `output.img`
for use with SimCoupe or another disk writing program:

```
writeusb image.dsk -o output.img
```

Converting non-bootable disks will add a special version of SAMDISK v2, patched
to dynamically support both 9-sector and 10-sector disks. It will appear in the
directory listing as `samdisk9`. When an existing boot loader is patched it
supports only the converted 9-sector disks.

## Troubleshooting

macOS and Linux users may need to run the script under `sudo`, depending on the
permissions and group ownership of the USB floppy device. Linux users may just
need to be in the `disk` group, depending on distribution.

Be sure to use real double-density media, which usually has a blue cover. High
density disks have different magnetic properties, so covering the density hole
is not a good solution. HD disks are often unreliable after writing (YMMV).

If you're reusing existing SAM disks be aware that some USB floppy drives may
not recognise the existing 10-sector format. You may have to reformat the disk
as true 9-sector before it'll work. Under Windows try `format a: /t:80 /s:9`, or
under Linux try `ufiformat /dev/sdX` (change sdX to the correct device name).

SAMDOS/MasterDOS/BDOS will retry after disk errors but custom loaders may not.
The MNEMOtech loader used by MNEMOdemo 1 and 2 fails immediately fails with a
Loading Error so you'll need good quality disks!

Expect disk errors. If in doubt try a different disk!

## Limitations

Disk images containing custom formats are not supported and will be rejected.
This prevents original copies of Lemmings, Prince or Persia, and maybe some
other titles from working.

Reducing from 10 sectors to 9 sectors also reduces the disk capacity. The
converted disk has 72 directory slots and 702K of free space, rather than 80
directory slots and 780K on a regular disk. Full disks may need to be split.

Disks storing data outside the normal filesystem structures will be missed by
the conversion process. This affects the Pac-Man Emulator (v1.4 or earlier).

----

https://github.com/simonowen/writeusb
