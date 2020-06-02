### Scrypt
  Scrypt is a windows Ransomware with discord integration. After trying to find a reason to procrastinate someone gave me the idea to speedrun making a ransomware, so I made this ransomware in 5 hours. Scrypt allows for easy reports and access without the hassle of setting up a VPS for testing. 
  
### Scrypt Attack Vectors
  Once you are hit by Scrypt you will instantly realize you are a victim. A giant screen warning the user (as shown below) will take up your entire screen, once you hit the continue button the window will become invisble so it can continue to run in the background. While I had wanted to use chacha20 for file encryption I ended up sticking to AES-128 due to my limited time.
 <p align="center">
  <img width="460" height="300" src="https://github.com/backslash/ScryptRansomware/blob/master/images/lockscreen.png?raw=true">
</p>
  
  Another feature of Scrypt is its easy report feature which gives you a detailed report of your victim, I used myself below as an example for how the data looks, this can be used to easily match client ID's.
 <p align="center">
  <img width="460" height="300" src="https://github.com/backslash/ScryptRansomware/blob/master/images/report.PNG?raw=true">
</p>

  Scrypt will also leave behind a nice little readme on the desktop just in case the client forgets any of his information. This will contain information such as your btc address, client, id and detailed steps to recovering there files. 
   <p align="center">
  <img width="460" height="300" src="https://github.com/backslash/ScryptRansomware/blob/master/images/note.PNG?raw=true">
</p>

### Setup
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
  
  
### Developers
  Hello fellow developers, if you are interested in contribuiting to Scrypt I will happily accept pushes for new features or improvements to the current version, this was made in 5 hours so its got a few things that could for sure use improvement:
  - [ ] Improve File Handeling (Change Extenstion not hard to do os.rename())
  - [ ] Give the decrypter a user interface.
  - [ ] Speed up the encryption proccess
  - [ ] Send more data/sensitive data via webhook.  
  
  
### README
  This is illegal if you use this without the consent of others, I am not accountable for anything you get into, this was just a speedrun to demonstrate how ransomware is made/looks. This is 100% educational. Please do not misuse this tool.

