# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdfdiff.py'],
             pathex=['C:\\Dev\\Python\\pdfminer.six_i\\tools'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['django','matplotlib','PIL','numpy','qt5'],
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
          name='pdfdiff',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
