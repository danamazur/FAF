from flask import Flask, render_template
import xmltodict
import json
# from pprint import pprint
#
app = Flask(__name__)
#
@app.route('/')
def index():
    return render_template('index.html', foo='ero')

#
# if __name__ == '__main__':
#     with open(r'C:\Users\sezgh\Downloads\Telegram Desktop\Hackathon\FCIM BUGET.xlsx') as in_file:
#         xml = in_file.read()
#         with open('jsondata.json', 'w') as out_file:
#             pprint(json.dump(xmltodict.parse(xml), out_file))

if __name__ == '__main__':
    app.run(debug=True)
