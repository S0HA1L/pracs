import java.util.*;
public class LoadBalancing{
static void printLoad(int servers, int processes) {
int each=processes/servers;
int extra=processes%servers;
int total=0;
int i=0;
for(i=0; i<extra; i++) {
System.out.println("Server "+(i+1)+" has "+(each+1)+" Processes");
}
for(;i<servers;i++) {
System.out.println("Server "+(i+1)+" has "+each+" Processes");
}
}
public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
System.out.print("Enter the number of Servers: ");
int servers=sc.nextInt();
System.out.print("Enter the number of Processes: ");
int processes=sc.nextInt();
while(true) {
printLoad(servers, processes);
System.out.println("1.Add Servers 2.Remove Servers 3.Add Processes 4.Remove Processes 5.Exit ");
switch(sc.nextInt()) {
case 1:
System.out.println("How many more servers to add ? ");
servers+=sc.nextInt();
break;
case 2:
System.out.println("How many more servers to remove ? ");
servers-=sc.nextInt();
break;
case 3:
System.out.println("How many more Processes to add ? ");
processes+=sc.nextInt();
break;
case 4:
System.out.println("How many more Processes to remove ? ");
processes-=sc.nextInt();
break;
case 5:
return;
}
}
}
}
