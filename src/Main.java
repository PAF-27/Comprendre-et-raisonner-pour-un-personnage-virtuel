import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	ArrayList<ArrayList<String>> test = JDOM1.XMLtoList("/home/erwan/Documents/PAF/Test/testout.xml");
	JDOM1.ListtoXML(test, "/home/erwan/Documents/PAF/Test/testjava.xml");
	}
}
