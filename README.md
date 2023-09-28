# DracoTube
DracoTube is a terminal application created using Google's YouTube Data API && third-party Pytube package.

Things script can do if setup properly:
* Search YouTube video
* Open video on your browser
* Download the video from YouTube
>Note: You're welcome to modify and use the source code under the license agreement. Reviews are welcome.

## Setup

### Python3 && Pip
Python3 is needed to run the script. It comes with pip (package installer). On most Linux systems, it is already installed. For other systems, install from https://www.python.org/downloads/

### Google Client API
You need to setup a project at https://developers.google.com. Navigate to Google API Console. Get an API key.
> Refer to https://developers.google.com/youtube/v3/quickstart/python for more details.
For Windows, run the command to install Google Client API.

```bash
pip install google-api-python-client
```


### Pytube
Run following command to install Pytube (used to download YouTube videos).

```bash
pip install pytube3
```

> There is an error in the package currently. Find the installed package. For me, it was C:\Users\<name>\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube. Go to line 301 in extract.py and change the string to "signatureCipher". Now you're good to go.

Docs: https://python-pytube.readthedocs.io/en/latest/

### Change resources\apiKey.txt
1. Get API key from your projects Credentials.
2. Copy & paste the key in the file. (empty during download of repository)
