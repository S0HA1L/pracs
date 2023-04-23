import java.util.*;
import java.io.*;
import java.net.*;
public class Server {
public static void main(String args[]) throws Exception{
//Server server = new Server();
ServerSocket MyServer = new ServerSocket(5000);
Socket ss = MyServer.accept();
DataInputStream din =new DataInputStream(ss.getInputStream());
DataOutputStream dout=new DataOutputStream(ss.getOutputStream());
BufferedReader br=new BufferedReader(new
InputStreamReader(System.in));
Server server = new Server();
String str="",str2="";
int sum = 0;
while(!str.equals("stop")){
str=din.readUTF();
if(str.equals("stop"))
break;
sum = sum + Integer.parseInt(str);
}
dout.writeUTF(Integer.toString(sum));
dout.flush();
din.close();
ss.close();
MyServer.close();
}
}
