# Complete Inputs
name = r'^[A-Za-z]{2,}$'
phone = r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
email = r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
empID = r'^\d{1,15}$'
zip = r'^\d{5}([-\s]?\d{4})?$'
city = r'^([a-zA-Z\u0080-\u024F]+(?:. |-| |\'))*[a-zA-Z\u0080-\u024F]+$'
bank = r'^\d{6}-?\d{4}$'
route = r'^\d{8}-?[\dA-Za-z]$'
float = r'^\d{1,9}(\.\d{1,2})?$'
commission = r'^0{0,2}(?:[0-9][0-9]?|100)$'
ssn = r'^(?!(000|666|9))\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}$'

# Valid Characters
nameChars = r'[A-Za-z]'
phoneChars = r'[\d\-\(\)\.\+\s]'
dsd = r'[\d\s-]'
bankChars = r'[\d-]'
routeChars = r'[\dA-Za-z-]'
floatChars = r'[\d\.]'

# Other
states = ['AL', 'AK', 'AZ', 'AR', 'AS', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'TT', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']
genValidationArgs: list[tuple[str, str, int, str]] = [(name, nameChars, 100, 'fname'), (name, nameChars, 100, 'lname'), (phone, phoneChars, 18, 'ophone'), (email, '.', 100, 'oemail'), (empID, r'\d', 15, 'id')]
perValidationArgs: list[tuple[str, str, int, str]] = [(city, '.', 100, 'city'), (zip, dsd, 10, 'zip'), (phone, phoneChars, 18, 'hphone'), (email, '.', 100, 'hemail')]
admValidationArgs: list[tuple[str, str, int, str]] = [(bank, bankChars, 11, 'bankinfo'), (route, routeChars, 10, 'route'), (float, floatChars, 12, 'salary'), (float, floatChars, 12, 'hourly'), (commission, r'\d', 3, 'commission'), (ssn, dsd, 11, 'ssn')]
