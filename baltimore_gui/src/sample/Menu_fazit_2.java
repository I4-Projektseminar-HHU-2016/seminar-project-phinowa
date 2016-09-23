package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;


public class Menu_fazit_2 extends Scene {

    private Button startmenue;
    private Button zurueck;
    private Label label_fazit;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu_fazit_2(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.label_fazit = new Label("Fazit - Teil 2\n ");
        this.label_text = new Label("Wer sicher leben moechte, sollte sich in einem der aeussersten Bezirke von Baltimore niederlassen. Dabei scheint es\nim Norden und Westen der Stadt ungefaehrlicher zu sein als im Sueden und Osten. Der unangefochtene Spitzenreiter\nCross-Country befindet sich beispielsweise am nordwestlichen Rand Baltimores, North Baltimore und Greater Roland\nPark im Norden, Dickeyville, drittsicherster Bezirk 2014, ganz im Westen, und Edmondson Village ebenfalls westlich.\nAllesamt Bezirke, die die niedrigste Kriminalitaetsrate der letzten Jahre hatten.\n\nWaehrend sich der Spitzenreiter Cross-Country auf einem niedrigen stabilen niedrigen Niveau haelt, schafft es\nDickeyville sogar, eine Senkung der Kriminalitaetsrate von 2010 im Vergleich zu 2014 von ueber 60% zu erreichen.\nAber nicht bei allen aeusseren Bezirken laeuft es so gut. In South Baltimore, 2010 noch unter den sichersten zehn\nBezirken der Stadt, ist die Kriminalitaetsrate stark angestiegen. Ebenso in Beechfield, Edmondson Village oder\nLoch Raven. Auch hat die Gesamtzahl von Bezirken, die eine Rate von unter 40 und 50, also vergleichsweise niedrig,\nhaben, im Vergleich von 2014 zu 2010 jeweils abgenommen.\n\nObwohl Baltimore also bei der Gesamtentwicklung der Sicherheit, vor allem in Teilen des zentralen Stadtkerns, auf\neinem guten Weg ist, sollte die Regierung nicht die augenscheinlich ''sicheren'' Bezirke aus den Augen verlieren,\nda dort die prozentuale Steigerung der Kriminalitaet besonders ausgepraegt ist.\nQuelle: http://en.wikipedia.org/\nBild: http://images.fineartamerica.com/images-medium-large-5/batimore-inner-harbor-calvert-koerber.jpg\n \n ");
        this.startmenue = new Button("Startmenue");
        this.zurueck = new Button("Zurueck");
        this.master = Master.getInstance();

        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(31, 100, 19, 100)); //Abstand der GUI-Komponenten zum Rand (top/right/bottom/left)
        box.setSpacing(15);
        box.getChildren().addAll(label_fazit, label_text, startmenue, zurueck);

        label_fazit.setId("ueberschrift_start_menu");

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.startmenue.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu());
            }
        });
        zurueck.setOnAction(new EventHandler<ActionEvent>()  {
            public void handle(ActionEvent event ) {
                Main.stage.setScene(Master.getInstance().getMenu_fazit());
            }
        });


    }

}
