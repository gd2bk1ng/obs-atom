#!/bin/bash
set -e

# Paths
SRC_DIR=~/obs-atom-build/obs-studio
BUILD_DIR=~/obs-atom-build/build
INSTALL_PREFIX=/usr/local
FFMPEG_DIR=~/ffmpeg-install/lib/cmake/ffmpeg

# Clean previous build
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

cd "$BUILD_DIR"

cmake -S "$SRC_DIR" -B "$BUILD_DIR" \
  -DENABLE_BROWSER=OFF \
  -DENABLE_WEBRTC=OFF \
  -DENABLE_SRT=ON \
  -DENABLE_RIST=ON \
  -DFFMPEG_DIR="$FFMPEG_DIR" \
  -DCMAKE_INSTALL_PREFIX="$INSTALL_PREFIX"

make -j$(nproc)
sudo make install

