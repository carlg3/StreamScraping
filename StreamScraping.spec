# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['StreamScraping.py'],
             pathex=['C:\\Users\\Carlo\\Desktop\\Git\\StreamScraping'],
             binaries=[('C:\\Python38\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe','.\\selenium\\webdriver')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='StreamScraping',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
