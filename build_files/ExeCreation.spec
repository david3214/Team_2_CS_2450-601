# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['../main.py'],
    pathex=[],
    binaries=[],
    datas=[('..\\Resources\\', 'Resources')],
    hiddenimports=['tkinter', 'passlib.handlers.pbkdf2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    icon=['..\\Resources\\images\\employee-image.png'],
    name='EmployeeViewer',
    debug=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    console=False,
    runtime_tmpdir=None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None)