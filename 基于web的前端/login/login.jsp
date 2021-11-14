
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>登录</title>

<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path;
%>

<link rel="stylesheet" href="<%=basePath%>/css/bootstrap.css">

<style>
	body {
        margin: 0;
        padding: 0;
        background: url(png/login.jpg);
		background-size: 1500px 860px;
        }

        .div {
            width: 400px;
            height: 500px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .head-div {
            width: 100px;
            height: 100px;
            border: 1px solid #999;
            border-radius: 50%;
            margin: 0 auto 10px auto;
            background: url(img/2.jpg) no-repeat;
            background-size: 100px 100px;
        }

        .sign-div {
            width: 400px;
            height: 300px;
            text-align: center;
            outline: none;
            border: 1px solid rgb(94, 92, 233);
            border-radius: 8px;
            background-color: rgba(172, 235, 243, .2);
            box-sizing: border-box;
        }

        .sign-div h1 {
            margin-bottom: 10px;
            color: rgb(29, 26, 26);
        }

        input {
            width: 250px;
            height: 44px;
            border: none;
            outline: none;
            box-sizing: border-box;
            display: block;
            padding: 0 16px;
        }

        .input-text {
            margin: 5px auto;
            border-radius: 16px;
            margin-top:20px;
        }

        .input-text:hover {
            border: 0.5px solid rgb(76, 76, 233);
            transition: 0.5s;
            border-radius: 4px;
        }

        .input-btn1 {
            margin-top:20px;
            margin-left:75px;
            width: 110px;
            border-radius: 44px;
            cursor: pointer;
            background-color: rgba(84, 175, 249, 0.8);
        }
        
        .input-btn2 {
            margin-top:20px;
            margin-right:75px;
            width: 110px;
            border-radius: 44px;
            cursor: pointer;
            background-color: rgba(84, 175, 249, 0.8);
        }
        

        .input-btn1:hover {
            color: #fff;
            font-size: 16;
            border-radius: 4px;
            transition: 0.5s;
            background-color: rgba(10, 138, 243, 0.8);
        }

        .input-btn2:hover {
            color: #fff;
            font-size: 16;
            border-radius: 4px;
            transition: 0.5s;
            background-color: rgba(10, 138, 243, 0.8);
        }
        .sign-div a {
            text-decoration: none;
            color: rgb(92, 61, 112);
            font-size: 14px;
            padding: 10px;
            transition: 0.8s;
            display: block;
        }

        a:hover {
            color: #FFF;
            background: rgba(0, 0, 0, .3);
            border-radius: 8px;
        }
        
        
</style>
</head>

<body>
	<div class="div">
        <div class="head-div"></div>
        <div class="sign-div">
            <form class="form-horizontal" action="login1.jsp" method="post">
                <h1>登录</h1>
                <input class="input-text" type="text" name="username" placeholder="帐号">
                <input class="input-text" type="password" name="pwd" placeholder="密码">
                <div align="left" style="float:left">
                     <input class="input-btn1" type="button" value="注册"onclick="window.location.href='register.jsp';">
                </div>
                <div align="right">
                <input class="input-btn2" type="submit" value="登录">
                </div>
               
            </form>
        </div>
    </div>
</body>


</html>
