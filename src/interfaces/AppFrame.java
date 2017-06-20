package interfaces;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 */
public class AppFrame extends JFrame {

    private TextArea textArea;

    ButtonGroup groupWordEmbedding;

    ButtonGroup groupClustering;


    public AppFrame() {
        this.setSize(400,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setMenu();
        addPanel();

        this.setVisible(true);
    }

    private void setMenu() {
        JMenuBar menuBar = new JMenuBar();

        JMenu wordEmbedding = new JMenu("Word Embedding");
        groupWordEmbedding = new ButtonGroup();
        JRadioButtonMenuItem conceptNet = new JRadioButtonMenuItem("Concept net");
        conceptNet.setSelected(true);
        groupWordEmbedding.add(conceptNet);
        JRadioButtonMenuItem word2Vec = new JRadioButtonMenuItem("Word2Vec");
        conceptNet.setSelected(true);
        groupWordEmbedding.add(word2Vec);
        JRadioButtonMenuItem gloVe = new JRadioButtonMenuItem("GloVo");
        gloVe.setSelected(true);
        groupWordEmbedding.add(gloVe);
        wordEmbedding.add(conceptNet);
        wordEmbedding.add(word2Vec);
        wordEmbedding.add(gloVe);
        menuBar.add(wordEmbedding);

        JMenu clustering = new JMenu("Clustering");
        groupClustering = new ButtonGroup();
        JRadioButtonMenuItem kMeans = new JRadioButtonMenuItem("k-means");
        kMeans.setSelected(true);
        JRadioButtonMenuItem meanShift = new JRadioButtonMenuItem("Mean Shift");
        meanShift.setSelected(true);
        groupClustering.add(kMeans);
        groupClustering.add(meanShift);
        clustering.add(kMeans);
        clustering.add(meanShift);
        menuBar.add(clustering);

        this.setJMenuBar(menuBar);
    }

    private void addPanel() {
        JPanel inputPanel = new JPanel();

        inputPanel.setLayout(new BoxLayout(inputPanel, BoxLayout.Y_AXIS));
        inputPanel.setOpaque(true);

        JButton enter = new JButton("Enter");
        enter.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println(getText());
                textArea.setText("");
                SwingUtilities.updateComponentTreeUI(textArea);

            }
        });

        textArea = new TextArea();

        Label label = new Label("Please enter a sentence:");

        inputPanel.add(label);
        inputPanel.add(textArea);
        inputPanel.add(enter);

        this.add(inputPanel);
    }

    public String getText() {
        return textArea.getText();
    }

    public ButtonModel getWordEmbedding() {
        return groupWordEmbedding.getSelection();
    }

    public ButtonModel getClustering() {
        return groupClustering.getSelection();
    }

}
