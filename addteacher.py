#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
if setdefault.check() == False :
    redirectURL = "/cgi-bin/login.py"
    print("Content-type: text/html")
    print()
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
con = connect.con
cur = connect.cur

default = setdefault.init()
content = """
    <form action="addpost.py" method="POST" enctype='multipart/form-data'>
    <div style = "display: inline-block;vertical-align: top;">
    <p>Полное имя</p>
    <input type="text" style = "width: 50em;" name = "name">
    <p>Напишите немного о нем</p>
    <textarea name="description" style="width: 50em;height: 50em;"></textarea>
    <br>
    <input type = "submit">
    </div>
    <div style = "display: inline-block; vertical-align: top;">
    <img id = "preview" src='/cats.JPG' alt = ''><br>
    <input id = "id_files" type = 'file' name = 'img' accept='image/png'><br>
    </div>
</form>

<script>
        var fileField = document.getElementById('id_files');
		var preview = document.getElementById('preview');
		fileField.addEventListener('change', function(event) {
    	for(var x = 0; x < event.target.files.length; x++) {
        (function(i) {
            var reader = new FileReader();
            reader.onload = function(event) {
                preview.setAttribute('src', event.target.result);
                preview.setAttribute('class', 'preview');
            }
            reader.readAsDataURL(event.target.files[x]);
        })(x);
    }
	}, false);
    </script>
"""

default = default.replace("_content_", content)
default = default.replace("_namepage_", "Добавить препода")

print("Content-type: text/html")
print()
print(default)