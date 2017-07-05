import java.io.*;
import java.util.ArrayList;

public class Convertisseur {

	public static void convertion (ArrayList<ArrayList<String>> frameList, String path)
	{
		int n = frameList.size();
		boolean isTransformed;
		for (int i = 0;i<n;i++)
		{
			ArrayList<String> frames = frameList.get(i);
			int m = frames.size();
			for (int j = 2;j<m;j= j+2)
				{
				String frame = frames.get(j);
				frame = frame.toLowerCase();
				isTransformed = false;
				try{
					File fichier = new File(path);
					InputStream ips=new FileInputStream(fichier); 
					InputStreamReader ipsr=new InputStreamReader(ips);
					BufferedReader readableFichier = new BufferedReader(ipsr);
					String ligne;
					while ((ligne=readableFichier.readLine())!=null){
						String[] ref = ligne.split(" ");
						String frameref = ref[0];
						if (frame.compareTo(frameref) == 0)
						{
							String imSchema = ref[1];
							frames.set(j, imSchema);
							isTransformed = true;
						}
					}
					readableFichier.close();
				}
				catch(Exception e)
				{
					e.printStackTrace();
				}
				if (!isTransformed & frame.contains("_"))
				{
					int k = frame.indexOf("_");
					String frameextraite = frame.substring(0, k);
					try{
						File fichier = new File(path);
						InputStream ips=new FileInputStream(fichier); 
						InputStreamReader ipsr=new InputStreamReader(ips);
						BufferedReader readableFichier = new BufferedReader(ipsr);
						String ligne;
						while ((ligne=readableFichier.readLine())!=null){
							String[] ref = ligne.split(" ");
							String frameref = ref[0];
							if (frameextraite.compareTo(frameref) == 0)
							{
								String imSchema = ref[1];
								frames.set(j, imSchema);
								isTransformed = true;
							}
						}
						readableFichier.close();
					}
					catch(Exception e)
					{
						e.printStackTrace();
					}
					
				}
				if (!isTransformed)
				{
					frames.set(j, "nope");
				}
			}
			frameList.set(i, frames);
		}
	}
}
