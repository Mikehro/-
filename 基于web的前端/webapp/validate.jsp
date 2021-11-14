<%@ page import="java.awt.image.BufferedImage" %>
<%@ page import="java.awt.*" %>
<%@ page import="java.util.Random" %>
<%@ page import="javax.imageio.ImageIO" %>

<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>validate</title>
</head>
<body>
<%
    response.setHeader("Cache-Control", "no-cache");
    //在内存中创建图像
    int width = 90, height = 30;
    BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
    //获取画笔
    Graphics g = image.getGraphics();
    //设定定背景颜色
    g.setColor(new Color(200, 200, 200));
    g.fillRect(0, 0, width, height);
    //随机获取验证码
    Random rnd = new Random();
    int randNum = rnd.nextInt(8999) + 1000;
    String randStr = String.valueOf(randNum);
    //将验证码放入session中
    session.setAttribute("randStr", randStr);
    //将验证码显示到图像中
    g.setColor(Color.black);
    g.setFont(new Font("", Font.PLAIN, 25));
    g.drawString(randStr, 15, 20);
    //产生干扰点
    for (int i = 0; i < 100; i++) {
        int x = rnd.nextInt(width);
        int y = rnd.nextInt(height);
        g.drawOval(x, y, 1, 1);
    }
    //输出图像到界面
    ImageIO.write(image, "JPEG", response.getOutputStream());
    out.clear();
    out = pageContext.pushBody();
%>
</body>
</html>

