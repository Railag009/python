import cgi
import cgitb; cgitb.enable()  # Для отладки ошибок

form = cgi.FieldStorage()

if 'Style' not in form or 'Materials' not in form or 'Price' not in form:
    print("Content-type: text/plain")
    print("Error: Some fields are missing.")
    exit()

style = form.getfirst("Style", "123")
materials = form.getfirst("Materials", "123")
price = form.getfirst("Price", "123")

print("Content-type: text/html")
print("""
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Architecture</title>
</head>
<body>
<h1>Architecture</h1>
<p>Style: %s </p>"""%style)
print("<p>Materials: %s</p>"%materials)
print("<p>Price: %s</p>"%price)
print("""<p>This form was processed successfully.</p>
</body>
</html>
""")