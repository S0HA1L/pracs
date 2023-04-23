 import java.io.*;
import java.net.*;

class cli {

    public static void main(String[] args) throws Exception {
        Socket sock = new Socket("127.0.0.1", 3000);
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);
        InputStream istream = sock.getInputStream();
        BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));
        System.out.println("Connected to the Server...");
        String receiveMessage, sendMessage, temp;
        while (true) {
            temp = keyRead.readLine();
            sendMessage = temp.toLowerCase();
            pwrite.println(sendMessage);
            sendMessage = keyRead.readLine();
            pwrite.println(sendMessage);
            sendMessage = keyRead.readLine();
            pwrite.println(sendMessage);
            System.out.flush();
            if ((receiveMessage = receiveRead.readLine()) != null) {
                System.out.println(receiveMessage);
            }
        }
    }
}
