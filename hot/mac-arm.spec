# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/chizongyang/code/python/install-demo/hot/main.py'],
    pathex=['/Users/chizongyang/code/python/install-demo/hot'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=['/Users/chizongyang/miniforge3/lib/python3.9/site-packages/pyupdater/hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mac-arm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
