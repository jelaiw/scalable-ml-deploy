## Overview
A quick, proof-of-concept implementation for the "Scalable ML Deploys for Data Science" design pattern described by Dan Sullivan (see References slide in `slides.pdf`).

See slides for further background and context.

## *picrunch* Algorithm Service (REST API)
Calculates pi to specified number of digits after the decimal.

Implements the *picrunch* algorithm by Don Cross. See https://medium.com/@cosinekitty/how-to-calculate-a-million-digits-of-pi-d62ce3db8f58 for further detail.

```
GET /api/v0/pi?ndigits=99
```

| Attribute | Type | Required | Description |
| ------ | ------ | ------ | ------ |
| ndigits | integer | no | Number of digits after the decimal to calculate pi. *Default is 22.* |

Example response:
```
{"ndigits":99,"pi":"3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"}
```
