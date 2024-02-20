from gtts import gTTS
import PyPDF2
import ebooklib
from ebooklib import epub
import os

MAX_FILE_SIZE_MB = 1,5  #  maximum file size allowed in megabytes

# Function to get file size in megabytes
def get_file_size_mb(file_path):
    """
    Get the size of a file in megabytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        float: The size of the file in megabytes.
    """
    return os.path.getsize(file_path) / (1024 * 1024)

# Function to convert PDF to text
def convert_pdf_to_txt(pdf_file):
    """
    Extracts the text from a PDF file and returns it as a string.

    Args:
        pdf_file (str): The path to the PDF file locally.

    Returns:
        str: Text from the PDF file.

    Raises:
        ValueError: If input file is not a PDF or if file size exceeds maximum limit.

    """
    if not pdf_file.endswith('.pdf'):
        raise ValueError('Input file must be a PDF file.')
    if get_file_size_mb(pdf_file) > MAX_FILE_SIZE_MB:
        raise ValueError(f'File size exceeds the maximum limit of {MAX_FILE_SIZE_MB} MB.')
    txt = ''
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            txt += page.extract_text()
    return txt

# Function to convert EPUB to text
def convert_epub_to_txt(epub_file):
    """
    Extracts the text from an EPUB file and returns it as a string.

    Args:
        epub_file (str): The path to the EPUB file locally.

    Returns:
        str: Text from the EPUB file.

    Raises:
        ValueError: If the input file is not an EPUB or if file size exceeds maximum limit.

    """
    if not epub_file.endswith('.epub'):
        raise ValueError('Input file must be an EPUB file.')
    if get_file_size_mb(epub_file) > MAX_FILE_SIZE_MB:
        raise ValueError(f'File size exceeds the maximum limit of {MAX_FILE_SIZE_MB} MB.')
    txt = ''
    book = epub.read_epub(epub_file)
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        txt += item.get_body_content().decode('utf-8')
    return txt

# Function to convert text to audio
def text_to_audio(text, output_file):
    """
    Convert text to audio and save it to mp3 file.

    Args:
        text (str): The text to convert to audio.
        output_file (str): The path and name of the output mp3 file.

    Returns:
        None
    """
    tts = gTTS(text)
    tts.save(output_file)


def main():
    input_file = input('Enter the path of the file you desire to convert to audio (PDF or EPUB): ')
    output_file = input('Enter the desired name of the output MP3 file (without extension): ') + '.mp3'

    if input_file.endswith('.pdf'):
        text = convert_pdf_to_txt(input_file)
    elif input_file.endswith('.epub'):
        text = convert_epub_to_txt(input_file)
    else:
        raise ValueError('Unsupported file format. Please enter a .pdf or .epub file.')

    text_to_audio(text, output_file)


if __name__ == '__main__':
    main()
