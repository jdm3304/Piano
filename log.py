#!/usr/bin/python

#Import modules for CGI handling
import cgi,cgitb

#Create instance of FieldStorage
form = cgi.FieldStorage()

#Get data from fields
login_id = form.getvalue('id')
password = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Piano 시작하기</title>"
print "</head>"
print "<body>"
print "<h2>안녕하세요. %s님.</h2>" % (login_id)
#print "<center>"
#print "<H3>Start 버튼을 눌러 피아노를 시작해보세요.</H3><br />"
#print "<form method=get action="cgi-bin/distance.py">"
#print "저장 버튼을 누를 시, 목록에서 저장된 파일이 보여집니다.<br />"
#print "정지 버튼을 눌러도 저장되지 않습니다.<br /><br /><br />"
#print "<input type="submit" name="Tstart" value="Start">"
#print "<input type="submit" name="stop" value="정지"><br /><br />"
#print "<input type="submit" name="commit" value="저장"><br /><br />"
#print "<a href=/cgi-bin/list.py">목록</a>"
#print "</form>"
#print "</center>"
print "</body>"
print "</html>"
