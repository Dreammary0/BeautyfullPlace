from flask import Flask, session

app = Flask(__name__)
# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.index
import controllers.reg_page
import controllers.master_page
import controllers.master_date_page
import controllers.date_page

if __name__ == '__main__':
    app.run()