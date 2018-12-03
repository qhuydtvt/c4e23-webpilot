from gmail import GMail, Message
from random import choice

gmail = GMail("c4e.techkidsvn@gmail.com", "codethechange")

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]

template = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay em ngủ dậy, thấy {{symptom}}, b&aacute;c sỹ bảo em bị Ebola.</p>
<p>Sếp cho em nghỉ l&agrave;m nh&eacute; <img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" />.</p>
<p>Nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" />,</p>
'''
sickness = choice(sickness_list)
symptom = "đau bụng"

content = template.replace("{{sick}}", sickness).replace("{{symptom}}", symptom)

message = Message("Xin nghỉ làm", to="qhuydtvt@gmail.com", html=content)

gmail.send(message)