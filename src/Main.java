import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
	//Runtime.getRuntime().exec("/home/erwan/Documents/PAF/semafor-semantic-parser/release/fnParserDriver.sh /home/erwan/Documents/PAF/Test/test.txt").waitFor();
	ArrayList<ArrayList<String>> test = JDOM1.XMLtoList("/home/erwan/Documents/PAF/Test/exemple2.out");
	Convertisseur.convertion(test,"/home/erwan/Documents/PAF/frametoimageschema/frames_to_imageschemas.txt");
	JDOM1.ListtoXML(test, "/home/erwan/Documents/PAF/Test/exemple2java.xml");
	}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}
