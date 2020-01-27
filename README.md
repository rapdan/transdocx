# transdocx.py#
## .docx document translator ##
## The program translates paragraphs of docx documents while maintaining the original content
Your Google token should be in the file my_token.json  
You can choose the target language (target variable).  
If you need to translate pdf files, I recommend [pdf2doc.com](https://pdf2doc.com) for conversion to docx document.

Starting the program: 
## How to install? ##
```bash
git clone https://github.com/rapdan/transdocx
pip install -r requirements.txt
```
## Create the Authentication Credentials ##
You need to first generate a JSON Key File through the Google Developers Console.   
[console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
![console_cloud](https://github.com/rapdan/transdocx/pic/console_cloud.png "Google console cloud")

Fill the form and choose a “JSON” key type:
![console_cloud](https://github.com/rapdan/transdocx/pic/create_json.png "Create json file")


Save a “JSON” key as my_token.json in program directory.

## How to translate? ##
```python
python transdocx.py document_name.docx  
```
(the document_name.docx must be in the program directory)
The result is saved with the prefix target e.g pl-document_name.docx
