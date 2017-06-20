import java.io.*;
import org.jdom2.*;
import org.jdom2.input.*;
import org.jdom2.filter.*;
import org.jdom2.output.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class JDOM1 {

	public static ArrayList<ArrayList<String>> XMLtoList(String path){
		org.jdom2.Document document;
	    Element racine;
	    
	    SAXBuilder sxb = new SAXBuilder();
	    ArrayList<ArrayList<String>> frameArray = new ArrayList<ArrayList<String>>();
	      try
	      {
	         //On crée un nouveau document JDOM avec en argument le fichier XML
	         //Le parsing est terminé ;)
	         document = sxb.build(new File(path));
	         
	          //On initialise un nouvel élément racine avec l'élément racine du document.
		      racine = document.getRootElement();
		      Iterator h = racine.getDescendants(new ElementFilter("sentence"));
		      while(h.hasNext())
		         {
		        	 Element sentence = (Element)h.next();
		        	 Iterator j = sentence.getDescendants(new ElementFilter("annotationSet"));
		        	 ArrayList<String> innerFrameArray = new ArrayList<String>();
		        	 innerFrameArray.add(sentence.getChildText("text"));
		        	 while (j.hasNext())
		        	 {
		        		 Element annotation = (Element)j.next();
		        		 innerFrameArray.add(annotation.getAttributeValue("frameName"));
		        	 }
		        	 frameArray.add(innerFrameArray);
		         }
	      }
	      catch(Exception e){
	    	  e.printStackTrace();
	      }
		return frameArray;
      }
	
	public static void ListtoXML (ArrayList<ArrayList<String>> imSchemaList,String fichier)
	{
		Element racine = new Element("sentences");
		org.jdom2.Document document = new Document(racine);
		int n = imSchemaList.size();
		for (int i = 0; i<n;i++)
		{
			ArrayList<String> imSchema = imSchemaList.get(i);
			Element sentence = new Element("sentence");
			racine.addContent(sentence);
			Element text = new Element("text");
			text.setText(imSchema.get(0));
			sentence.addContent(text);
			Element annotationSets = new Element("annotationSets");
			sentence.addContent(annotationSets);
			int m = imSchema.size();
			for (int j = 1;j<m;j++)
			{
				Element annotationSet = new Element("annotationSet");
				annotationSets.addContent(annotationSet);
				Attribute imageSchema = new Attribute("imageSchema",imSchema.get(j));
				annotationSet.setAttribute(imageSchema);
			}
		}
		try
		   {
		      //On utilise ici un affichage classique avec getPrettyFormat()
		      XMLOutputter sortie = new XMLOutputter(Format.getPrettyFormat());
		      //Remarquez qu'il suffit simplement de créer une instance de FileOutputStream
		      //avec en argument le nom du fichier pour effectuer la sérialisation.
		      sortie.output(document, new FileOutputStream(fichier));
		   }
		   catch (java.io.IOException e){
			   e.printStackTrace();
		   }
	}
}

