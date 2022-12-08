# Complete Inputs
name = '^[\w\'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]*$'
phone = '^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
email = '(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
empID = '^\d{1,15}$'
date = '^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
zip = '^\d{5}([-\s]?\d{4})?$'
city = '^([a-zA-Z\u0080-\u024F]+(?:. |-| |\'))*[a-zA-Z\u0080-\u024F]+$'
bank = '^\d{6}-?\d{4}$'
route = '^\d{8}-?[\dA-Za-z]$'
float = '^\d{1,9}(\.\d{1,2})?$'
commission = '^0{0,2}(?:[0-9][0-9]?|100)$'
ssn = '^(?!(000|666|9))\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}$'

# Valid Characters
phoneChars = '[\d\-\(\)\.\+\s]'
dateChars = '[\d/\-\.]'
dsd = '[\d\s-]'
bankChars = '[\d-]'
routeChars = '[\dA-Za-z-]'
floatChars = '[\d\.]'

# Other
states = ['AL', 'AK', 'AZ', 'AR', 'AS', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'TT', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']
genValidationArgs = [(name, '.', 100, 'fname'), (name, '.', 100, 'lname'), (phone, phoneChars, 18, 'ophone'), (email, '.', 100, 'oemail'), (empID, '\d', 15, 'id'), (date, dateChars, 10, 'sDate'), (date, dateChars, 10, 'eDate')]
perValidationArgs = [(city, '.', 100, 'city'), (zip, dsd, 10, 'zip'), (phone, phoneChars, 18, 'hphone'), (email, '.', 100, 'hemail')]
admValidationArgs = [(bank, bankChars, 11, 'bankinfo'), (route, routeChars, 10, 'route'), (float, floatChars, 12, 'salary'), (float, floatChars, 12, 'hourly'), (commission, '\d', 3, 'commission'), (date, dateChars, 10, 'dob'), (ssn, dsd, 11, 'ssn')]