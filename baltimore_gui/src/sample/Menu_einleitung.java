package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;


public class Menu_einleitung extends Scene {

    private Button weiter;
    private Button zurueck;
    private Label label_einleitung;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu_einleitung(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.label_einleitung = new Label("Einleitung\n ");
        this.label_text = new Label("Im Rahmen dieses Projektes moechte ich die Entwicklung von Verbrechen in Baltimore in den letzten Jahren untersuchen.\nDazu habe ich eine CSV-Datei ausgesucht, die Auskunft ueber die Kriminalitaetsrate und verschiedene Verbrechen wie\nGewalt, Diebstahl, haeusliche Gewalt und Schusswaffentoetung in saemtlichen Bezirken von Baltimore gibt. Die 620.000\nEinwohner umfassende Ostkuestenstadt der USA ''hat unter den US-amerikanischen Grossstaedten am staerksten mit\nArmut, Verwahrlosung, Drogenabhaengigkeit und Suburbanisierung zu kaempfen'' (wikipedia.de, o.S.) und ist fuer diese\nUntersuchung deshalb besonders interessant.\n\nUnter anderem moechte ich Fragen beantworten wie: Hat die Verbrechenslage im Laufe der letzten Jahre zu- oder\nabgenommen? In welchen Stadtbezirken lebt es sich am sichersten, in welchen am gefaehrlichsten? Wie ist die\nEntwicklung im ''sichersten'' und ''gefaehrlichsten'' Bezirk hinsichtlich mehrerer Faktoren? Und wie sieht die Entwicklung\nbezueglich der Faktoren in ganz Baltimore ueber die Jahre hinweg aus?\n\nAm Ende folgt eine abschliessende Zusammenfassung und Diskussion der Ergebnisse, in der ich moegliche Ursachen fuer\ndiese betrachte, indem ich fuer auffaellige Bezirke kleine Hintergrundchecks durchfuehre.\n ");
        this.weiter = new Button("Weiter");
        this.zurueck = new Button("Zurueck");
        this.master = Master.getInstance();

        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(30, 100, 0, 100)); //Abstand der GUI-Komponenten zum Rand (top/right/bottom/left)
        box.setSpacing(15);
        box.getChildren().addAll(label_einleitung, label_text, weiter, zurueck);

        label_einleitung.setId("ueberschrift_start_menu");

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.weiter.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu_1());
            }
        });
        zurueck.setOnAction(new EventHandler<ActionEvent>()  {
            public void handle(ActionEvent event ) {
                Main.stage.setScene(Master.getInstance().getMenu());
            }
        });


    }

}
