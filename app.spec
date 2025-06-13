# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\AngiePaolaCanacueyRo\\OneDrive - kyndryl\\Documentos\\Mis Box Notes\\AUTOMATIZACION\\buscador_web_equipo'],
    binaries=[],
    datas=[
        ('Información de equipos.xlsx', '.'), 
        ('logo.jpg', '.'),  # si usas un logo en tu app
    ],
    hiddenimports=['streamlit'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BuscadorEquipos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False  # Cambia a True si quieres ver consola
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BuscadorEquipos'
)
