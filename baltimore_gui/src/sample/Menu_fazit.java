package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;


public class Menu_fazit extends Scene {

    private Button weiter;
    private Button zurueck;
    private Label label_fazit;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu_fazit(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.label_fazit = new Label("Fazit - Teil 1\n ");
        this.label_text = new Label("Alles in allem scheint die Kriminalitaet fuer ganz Baltimore betrachtet in saemtlichen Faktoren konstant leicht\nabzunehmen. Die Verbrechenslage hat sich im Laufe der Jahre also verbessert. Ein Erfolg fuer die in den letzten\nJahrzehnten in Verruf geratene Ostkuestenstadt der USA. Am gefaehrlichsten lebt es sich dabei in Downtown,\nam sichersten ist der Bezirk Cross-Country.\n\nBezirke, die den geografischen Mittelpunkt Baltimores bilden, wie die Innenstadt Downtown, die direkt suedlich\nangrenzenden Hafenbezirke Inner Harbor und East Harbor, der westlich anliegende Bezirk Washington Village,\nGreater Mondawmin nordwestlich und Midtown noerdlich von Downtown leiden besonders unter hoher Kriminalitaet.\nSie alle finden sich in den Top-10 der Kriminalitaetsrate wieder.\n\nDass der Kern Baltimores das grosse Problem ist, scheint die Regierung erkannt zu haben: Die ''Brandherde'' Downtown\nund Inner Harbor weisen seit 2010 eine beeindruckende Verbesserung der Sicherheitslage auf: In jedem Jahr bis 2014\nsank dort die Kriminalitaetsrate, bei Downtown um fast 80% und beim Hafengebiet um ueber 100% im Vergleich von\n2010 zu 2014. Auch das suedlich befindliche Brooklyn hat eine achtbare Veraenderung zum Besseren vorzuweisen.\nDiese positive Entwicklung sollte beibehalten werden, und auch auf die anderen angrenzenden zentralen Bezirke\nausgeweitet werden, bei denen teilweise eine Stagnation der hohen Kriminalitaetsrate vorliegt oder sogar stark steigt,\nwie z.B. beim oestlichen Hafengebiet East Harbor.\n \n \n ");
        this.weiter = new Button("Weiter");
        this.zurueck = new Button("Zurueck");
        this.master = Master.getInstance();

        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(31, 100, 19, 100)); //Abstand der GUI-Komponenten zum Rand (top/right/bottom/left)
        box.setSpacing(15);
        box.getChildren().addAll(label_fazit, label_text, weiter, zurueck);

        label_fazit.setId("ueberschrift_start_menu");

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.weiter.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu_fazit_2());
            }
        });
        zurueck.setOnAction(new EventHandler<ActionEvent>()  {
            public void handle(ActionEvent event ) {
                Main.stage.setScene(Master.getInstance().getMenu_30());
            }
        });


    }

}
