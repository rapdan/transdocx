
import os
import re
from docx import Document
from google.cloud import translate_v2 as translate

# Create your own account in Google Cloud Platform and generate a file .json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'my_token.json'
target = 'pl'  # you can change to another language
g_tr = translate.Client()  # utworzenie instancji klasy translatora


def doc_trans(fn):
    ''' Translate docx document '''
    doc = Document(fn)

    for para in doc.paragraphs:  # petla po paragrafach
        if para.text != "":  # jezeli paragraf nie jest pusty probuj tłumaczyc
            try:
                tr_raw = g_tr.translate(para.text, target_language=target)
                tr = tr_raw['translatedText']
            except Exception as e:
                print(
                    'Google Translation error, check connection or your google token', e)
                return
            para.text = re.sub(para.text, para.text + '\n' + tr, para.text)
            # paragraph.text = re.sub("USERNAME", "John", paragraph.text)
            print(para.text)

    # save
    n_dir = os.path.dirname(fn)
    n_file = os.path.basename(fn)
    to_save = os.path.join(n_dir, target+'-'+n_file)
    doc.save(to_save)


if __name__ == '__main__':
    from sys import argv
    fn = argv[1]    # nazwa pliku docx do tłumaczenia
    doc_trans(fn)
