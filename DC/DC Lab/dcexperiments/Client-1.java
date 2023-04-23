import java.io.*;
import java.util.*;
import java.net.*;
public class Client
{
public static void main(String args[])throws Exception
{
String send="",r="";
Socket MyClient = new Socket("127.0.0.1",5000);
DataInputStream din=new
DataInputStream(MyClient.getInputStream());
DataOutputStream dout = new
DataOutputStream(MyClient.getOutputStream());
Scanner sc = new Scanner(System.in);
while(!send.equals("stop")){
System.out.print("Send: ");
send = sc.nextLine();
dout.writeUTF(send);
}
dout.flush();
r=din.readUTF();
System.out.println("Reply: "+ r);
dout.close();
din.close();
MyClient.close();
}
}
