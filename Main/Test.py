name = "Alice"
age = 30

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>User Information</title>
</head>
<body>
    <h1>Welcome, {name}!</h1>
    <p>You are {age} years old.</p>
</body>
</html>
"""

# Use f-strings (Python 3.6+) for easy variable insertion
rendered_html = html_template.format(name=name, age=age)

# Write the rendered HTML to a file
with open("user_info.html", "w") as f:
    f.write(rendered_html)