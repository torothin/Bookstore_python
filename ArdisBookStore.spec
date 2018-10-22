# -*- mode: python -*-

block_cipher = None


a = Analysis(['ArdisBookStore.py'],
             pathex=['C:\\Users\\Owner\\Dropbox\\Python Mega Course\\App 5 Bookstore with Tkinter and SQL'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ArdisBookStore',
          debug=False,
          strip=False,
          upx=True,
          console=False )
