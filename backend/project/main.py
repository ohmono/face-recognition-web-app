from flask import Flask
import app.views as views

# app
app = Flask(__name__)

app.add_url_rule('/base', 'base', views.base)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/faceapp', 'faceapp', views.faceapp)
app.add_url_rule('/faceapp/gender', 'gender',
                 views.gender, methods=['GET', 'POST'])
# run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
