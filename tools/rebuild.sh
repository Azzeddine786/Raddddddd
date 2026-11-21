#!/bin/sh
# Regenerates the whole site from the original Arabic source + the content files in this folder.
# Usage (from the repo root):  sh tools/rebuild.sh   -> writes ./site-out
set -e
cd "$(dirname "$0")/.."
rm -rf /tmp/rm-src && mkdir -p /tmp/rm-src && unzip -q tools/source-original.zip -d /tmp/rm-src
python3 tools/build.py /tmp/rm-src/Raddddddd-main ./site-out
python3 tools/qa.py ./site-out
