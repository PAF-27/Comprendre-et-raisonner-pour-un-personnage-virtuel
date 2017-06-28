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
		        	 String text = sentence.getChildText("text");
		        	 innerFrameArray.add(text);
		        	 while (j.hasNext())
		        	 {
		        		 Element annotation = (Element)j.next();
		        		 Iterator k = annotation.getDescendants(new ElementFilter("layer"));
		        		 while (k.hasNext()){
		        			 Element layer = (Element)k.next();
		        			 String name = layer.getAttributeValue("name");
		        			 if (name.compareTo("Target") == 0)
		        			 {
		        				 Element label = layer.getChild("labels").getChild("label");
		        				 innerFrameArray.add(label.getAttributeValue("end"));
		        			 }
		        		 }
		        		 innerFrameArray.add(annotation.getAttributeValue("frameName"));
		        	 }
		        	 int m = innerFrameArray.size();
		        	 for (int i =0;i<(m-1)/2;i++)
		        	 {
		        		 for (int l = 1;l<m-2;l=l+2)
		        		 {
		        			 if (Integer.parseInt(innerFrameArray.get(l)) > Integer.parseInt(innerFrameArray.get(l+2)))
		        			 {
		        				 String aux = innerFrameArray.get(l);
		        				 innerFrameArray.set(l, innerFrameArray.get(l+2));
		        				 innerFrameArray.set(l+2, aux);
		        				 aux = innerFrameArray.get(l+1);
		        				 innerFrameArray.set(l+1, innerFrameArray.get(l+3));
		        				 innerFrameArray.set(l+3, aux);
		        			 }
		        		 }
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
			int compteur = 1;
			Element racine = new Element("imageschemainterpreter");
			org.jdom2.Document document = new Document(racine);
			int n = imSchemaList.size();
			Element imageschemas = new Element("imageschemas");
			racine.addContent(imageschemas);
			Element speech = new Element("speech");
			racine.addContent(speech);
			for (int i = 0; i<n;i++)
			{
				ArrayList<String> imSchema = imSchemaList.get(i);
				String text = imSchema.get(0);
				int m = imSchema.size();
				int position = 0;
				for (int j = 1;j<m;j = j+2)
				{
					if (imSchema.get(j+1).compareTo("nope") != 0)
					{
						Element tm = new Element("tm");
						Element imageschema = new Element("imageschema");
						speech.addContent(tm);
						imageschemas.addContent(imageschema);
						Attribute id = new Attribute("id","tm"+compteur);
						Attribute ref = new Attribute("ref","tm"+compteur);
						Attribute value = new Attribute("value",imSchema.get(j+1).toUpperCase());
						tm.setAttribute(id);
						imageschema.setAttribute(ref);
						imageschema.setAttribute(value);
						String sentence = text.substring(position, Integer.parseInt(imSchema.get(j))+1);
						position = Integer.parseInt(imSchema.get(j)) + 1;
						speech.addContent(sentence);
						compteur = compteur + 1;
					}
				}
				if (text.length() > position)
				{
					String sentence = text.substring(position);
					Element tm = new Element("tm");
					speech.addContent(tm);
					Attribute id = new Attribute("id","tm"+compteur);
					tm.setAttribute(id);
					speech.addContent(sentence);
					compteur = compteur + 1;
				}
			}
			Element tm = new Element("tm");
			speech.addContent(tm);
			Attribute id = new Attribute("id","tm"+compteur);
			tm.setAttribute(id);
			compteur = compteur + 1;
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

