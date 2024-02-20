# Audio maker
Reads the line of a PDF or EPUB file to make a audio, using the gtts library to do so.

## How to run locally
To run this program you only need to have python installed and install in your virtualenv the required packages.

To install all packages used we use the following command:

```shell
pip install -r requirements.txt
```

Then run the following command to run the program:

```shell
python main.py
```

The input in the program should be the path to the file in your computer's home directory and the name you want for the audio file.

Example:

```shell
/Users/giovana/Downloads/DataBaseArticle.pdf
```


## Import details about the project
Since gTTS is a Python library and CLI tool to interface with Google Translate's text-to-speech API, it only accepts a certain number of requests at a time. Therefore, the maximum size that can be used at once is 65 pages or 1.5 MB.