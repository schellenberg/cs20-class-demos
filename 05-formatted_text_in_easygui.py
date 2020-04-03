import easygui_qt as easy

title = "Demo for Ozayr"
random_word = "rabbit"

some_html = f"""
<h1>{title}</h1>
<p>This is just an example of <em>{random_word}</em> of the things you can
do when rendering HTML. There are many more things you could do:</p>

<ul>
    <li>other HTML tags you learn</li>
    <li>including images</li>
    <li>much more!</li>
</ul>"""

easy.show_html("Demo", some_html)