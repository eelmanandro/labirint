# -*- mode: python ; coding: utf-8 -*-
import os
pathex = [
    os.path.abspath("."), 
    "asstets", 
]

datas = [
    ("assets/background.jpg", "assets"),
    ("assets/cyborg.png", "assets"),
    ("assets/hero.png", "assets"),
    ("assets/treasure.png", "assets"),
    ("assets/jungles.ogg", "assets"),
    ("assets/money.ogg", "assets"),
    ("assets/kick.ogg", "assets"),
    ("assets/icon.ico", "assets"),
    ("assets/icon.png", "assets"),
]

a = Analysis(
    ['main.py'],
    pathex= pathex,
    binaries=[],
    datas= datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='labirint',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon = "assets/icon.ico",
)

