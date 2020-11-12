from flask import Flask
app = Flask(__name__)

@app.route('/api/v0/picrunch/<int:ndigits>')
#   This is picrunch.py by Don Cross with minor adaptation to REST API.
#
#   Use Machin's Formula
#   pi = 4*(4*arctan(1/5) - arctan(1/239))
#   to calculate pi to ndigit places after the decimal.
def picrunch(ndigits):
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
