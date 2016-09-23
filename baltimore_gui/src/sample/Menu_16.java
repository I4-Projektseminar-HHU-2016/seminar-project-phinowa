package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;


public class Menu_16 extends Scene {

    private Image image;
    private Button weiter;
    private Button zurueck;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu_16(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.image = new Image("figure_18.png");
        ImageView iv1 = new ImageView();
        iv1.setImage(image);
        iv1.setFitWidth(794);
        iv1.setFitHeight(397);
        this.label_text = new Label("Nur in Loch Raven, das anfangs noch unter den zehn sichersten Bezirken zu finden war, ist die Kriminalitaetsrate von 2010\nbis 2014 in jedem Jahr gestiegen. Insgesamt faellt auf, dass eher bei Bezirken mit einer niedrigeren Rate haeufiger\nSteigungen auftreten als bei Bezirken mit einer hohen Kriminalitaetsrate.");
        this.weiter = new Button("Weiter");
        this.zurueck = new Button("Zurueck");
        this.master = Master.getInstance();

        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(0, 50, 0, 50)); //Abstand der GUI-Komponenten zum Rand (top/right/bottom/left)
        box.setSpacing(15);
        box.getChildren().addAll(iv1, label_text, weiter, zurueck);

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.weiter.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu_17());
            }
        });
        zurueck.setOnAction(new EventHandler<ActionEvent>()  {
            public void handle(ActionEvent event ) {
                Main.stage.setScene(Master.getInstance().getMenu_15());
            }
        });


    }

}
