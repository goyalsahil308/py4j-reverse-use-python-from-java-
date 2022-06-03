package py4j;
import py4j.GatewayServer;

public class Exam {
    public static void main(String[] args) {
          GatewayServer.turnLoggingOff();
          GatewayServer server = new GatewayServer();
          server.start();
          IHello hello = (IHello) server.getPythonServerEntryPoint(new Class[] { IHello.class });
          try {
              String y=hello.sayHello(2, "Sahil Goyal");
              System.out.println(y);
              int z=hello.minus(25, 35);
              System.out.println(z);
              int x=hello.multi(25, 35);
              System.out.println(x);
              int w=hello.plus(33, 66);
              System.out.println(w);
          } catch (Exception e) {
              e.printStackTrace();
          }
          server.shutdown();
    }
}