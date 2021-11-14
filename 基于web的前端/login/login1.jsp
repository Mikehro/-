<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>login1</title>
</head>
<body>
<%
String username=request.getParameter("username");
String pwd=request.getParameter("pwd");
int flag=0;
String url = "jdbc:mysql://rm-bp1y78ry9s88298yfzo.mysql.rds.aliyuncs.com:3306/user";
String sqlname = "huangdong0122";
String sqlpass = "Huangdong521";
try{
	Class.forName("com.mysql.jdbc.Driver");
    Connection conn=DriverManager.getConnection(url,sqlname,sqlpass);
    Statement Statement=conn.createStatement();
    String sql="select * from user1" ;
    ResultSet rs=Statement.executeQuery(sql);
    while(rs.next()){
    	if(rs.getString("username").equals(username)&&rs.getString("pwd").equals(pwd)){
    		flag=1;
    		out.print("<script>alert('登录成功！');location.href='index.html';</script>");
    	}
    }
    if(flag==0)
    	out.print("<script>alert('账号或密码错误！');location.href='login.jsp';</script>");
 }
catch(Exception e){
	out.print("连接异常");
}
%>
</body>
</html>
