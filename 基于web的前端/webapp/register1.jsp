<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>register1</title>
</head>
<body>
<%
String username=request.getParameter("username");
String pwd=request.getParameter("pwd");
String driver = "com.mysql.jdbc.Driver";  //加载驱动程序，不用改
String url = "jdbc:mysql://rm-bp1y78ry9s88298yfzo.mysql.rds.aliyuncs.com:3306/user";
try{
    Class.forName(driver);
    Connection conn=DriverManager.getConnection(url,"huangdong0122","Huangdong521");
    Statement Statement=conn.createStatement();
    String sql="select * from user1" ;
    ResultSet rs=Statement.executeQuery(sql);
    while(rs.next()){
    	if(rs.getString("username").equals(username))
    		out.print("<script>alert('用户名已被注册过！');location.href='register.jsp';</script>");
    }
    String rand = (String)session.getAttribute("randStr");
    String  input= request.getParameter("code");
    if(rand.equals(input)){
    	String sql1="insert into user1 values ('"+username+"','"+pwd+"')";
    	Statement.executeUpdate(sql1);
    	out.print("<script>alert('注册成功！');location.href='login.jsp';</script>");
    } else{
    out.print("<script>alert('请输入正确的验证码！');location.href='register.jsp';</script>");
    }
 }
catch(Exception e){
	out.print("连接异常");
}
%>
</body>
</html>