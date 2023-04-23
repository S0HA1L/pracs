import java.util.*;
public class Berkeley
{
public static int getTime(String time)
{
String[] temp = time.split(":");
int rtime = Integer.parseInt(temp[2]) + Integer.parseInt(temp[1])*60 +
Integer.parseInt(temp[0])*60*60;
return rtime;
}
public static String setTime(int time)
{
String rtime = new String();
for(int i=0;i<2;i++)
{
int power = (int)(Math.pow(60,2- i));
if((time/power)/10>0)
rtime = rtime + time/power;
else
rtime = rtime + "0" + time/power;
time = time%power;
rtime = rtime + ":";
}
if(time/10>0)
rtime = rtime + time;
else
rtime = rtime + "0" + time;
return rtime;
}
public static void main (String args[])
{
Scanner sc = new Scanner(System.in);
System.out.print("Enter number of machines: ");
int n = sc.nextInt();
String times[] = new String[n];
System.out.println("\nEnter current time of machines (HH:mm:ss) : ");
for(int i=0;i<n;i++)
{
System.out.print("Machine " + i + ": ");
times[i] = new String();
times[i] = sc.next();
}
System.out.println("\nStarting Simulation!\nMachine 0 is assumed as server and starts synchronization process.");
int st = getTime(times[0]);
int tot=0;
for(int i=0;i<n;i++)
{
System.out.println("Machine 0 sends TIME = " + times[0] + " to Machine " + i);
int diff = getTime(times[i])-st;
System.out.println("Machine " + i + " replies " + diff + " to Machine 0");
tot+=diff;
}
int avg = tot/n;
times[0] = setTime(st+avg);
System.out.println("\nMachine 0 sets new TIME = " + times[0] + " and sends it to all other machines.");
System.out.println("All machines set their time to "+ times[0]);
}
}
