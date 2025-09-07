#!/usr/bin/env python3
"""
obs-atom-installer.py
Flashy PyQt6 installer for OBS-Atom (32-bit friendly UI)
Save to: ~/obs-atom-build/obs-atom-installer.py
Run: python3 obs-atom-installer.py
"""

import os
import sys
import shutil
import subprocess
import json
import time
import threading
from pathlib import Path
from datetime import datetime

# Attempt PyQt6 import
try:
    from PyQt6 import QtWidgets, QtGui, QtCore
except Exception as e:
    print("PyQt6 is required. Install with: pip3 install --user PyQt6")
    raise

HOME = Path.home()
BASE = HOME / "obs-atom-build"
OBS_SRC = BASE / "obs"                 # Must exist (git clone --recursive)
BUILD_ROOT = BASE / "build"
BUILD_DIR = BUILD_ROOT / "obs"
LOG_DIR = BUILD_ROOT / "logs"
DEPS_DIR = BASE / "deps"
SIMDE_DIR = DEPS_DIR / "simde"
INSTALL_LEAN = BUILD_ROOT / "obs-install-lean"
INSTALL_ENH = BUILD_ROOT / "obs-install-enhanced"
INSTALL_LINK = BUILD_ROOT / "obs-install"

# Ensure directories exist
for d in (BASE, BUILD_ROOT, LOG_DIR, DEPS_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Restore point message
RESTORE_BLOCK = """
============================================================
🦝✨ Restore Point — Einstein the Raccoon (8K, time-traveled coder) ✨🦝
Stage [{stage}] completed successfully.
OBS-Atom Build Checkpoint Saved — You can safely resume from here!
============================================================
"""

# Helper: thread-safe append to QTextEdit via signals
class StreamSignals(QtCore.QObject):
    append_text = QtCore.pyqtSignal(str)
    stage_update = QtCore.pyqtSignal(str, int)  # stage_name, percent

# Worker thread that runs the build commands and streams output
class BuildWorker(QtCore.QRunnable):
    def __init__(self, mode, signals):
        super().__init__()
        self.mode = mode
        self.signals = signals
        self.env = os.environ.copy()
        # PKG_CONFIG paths if user has custom ffmpeg/srt/rist in home
        fpf = HOME / "ffmpeg-install" / "lib" / "pkgconfig"
        spf = HOME / "srt-install" / "lib" / "pkgconfig"
        rpf = HOME / "rist-install" / "lib" / "pkgconfig"
        pkg_paths = []
        for p in (fpf, spf, rpf):
            if p.exists():
                pkg_paths.append(str(p))
        if pkg_paths:
            self.env["PKG_CONFIG_PATH"] = ":".join(pkg_paths) + ":" + self.env.get("PKG_CONFIG_PATH", "")
        # LD_LIBRARY to prefer local libs
        ld_paths = []
from pathlib import Path

HOME = Path.home()

# pkg-config paths for dependencies
pkg_config_paths = {
    "FFmpeg": HOME / "dev/projects/obs-atom/obs-atom-build/ffmpeg-install/lib/pkgconfig",
    "SRT":    HOME / "dev/projects/obs-atom/obs-atom-build/srt-install/lib/pkgconfig",
    "RIST":   HOME / "dev/projects/obs-atom/obs-atom-build/rist-install/lib/pkgconfig"
}

print("\n🔍 Checking dependency pkg-config paths...\n")

all_found = True
for name, path in pkg_config_paths.items():
    if path.exists():
        print(f"✅ {name}: found at {path}")
    else:
        print(f"⚠️  {name}: NOT found at {path}")
        all_found = False

if all_found:
    print("\n🎉 All dependencies detected! The raccoon is doing backflips and fireworks are going off!\n")
else:
    print("\n⚡ Some dependencies are missing. The raccoon looks concerned. Check the warnings above.\n")
