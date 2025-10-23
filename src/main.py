from flask import Flask, views

app = Flask(__name__)

class MainView(views.MethodView):
    def get(self):
        return "Hello, world!"

# Register the view
app.add_url_rule('/', view_func=MainView.as_view('main'))


app.debug = True
app.run(port=30002)
