from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api/v0/pi')
# Implement picrunch algorithm described by Don Cross as a REST API.
def picrunch():
	# See https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object.
	# Default to ndigits of 22.
	# See https://werkzeug.palletsprojects.com/en/1.0.x/datastructures/#werkzeug.datastructures.MultiDict.
	ndigits = request.args.get('ndigits', default=22, type=int)
	return picrunch(ndigits)

def picrunch(ndigits):
	"""Return value of pi to ndigit places after the decimal.

	Implement picrunch algorithm described by Don Cross.

	Use Machin's Formula
	pi = 4*(4*arctan(1/5) - arctan(1/239))
	to calculate pi to ndigit places after the decimal.

	Examples:
	>>> picrunch(8)
	ArctanDenom(5) took 14 iterations.
	ArctanDenom(239) took 4 iterations.
	{'pi': '3.14159265', 'ndigits': 8}

	Args:
		ndigits: Number of places after the decimal as an int.

	Returns:
		Dict with value of pi as a string and ndigits as an int.
	"""
	xdigits = 10             # Extra digits to reduce trailing error

	# Use Machin's Formula to calculate pi.
	pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))

	# We calculated extra digits to compensate for roundoff error.
	# Chop off the extra digits now.
	pi //= 10**xdigits

	# Insert the decimal point after the first digit '3'.
	text = str(pi)
	return {
		'pi': text[0] + "." + text[1:],
		'ndigits': ndigits,
	}

def ArctanDenom(d, ndigits):
	# Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
	total = term = (10**ndigits) // d
	n = 0
	while term != 0:
		n += 1
		term //= -d*d
		total += term // (2*n + 1)
	print('ArctanDenom({}) took {} iterations.'.format(d, n))
	return total
