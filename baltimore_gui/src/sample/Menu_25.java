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


public class Menu_25 extends Scene {

    private Image image;
    private Button weiter;
    private Button zurueck;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu_25(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.image = new Image("figure_15.png");
        ImageView iv1 = new ImageView();
        iv1.setImage(image);
        iv1.setFitWidth(794);
        iv1.setFitHeight(397);
        this.label_text = new Label("Auch in Cross-Country wird am wenigsten Diebstahl ausgeuebt. Dickeyville ueberrascht mit einem souveraenen diebstahlsicheren\nzweiten Platz. Im Gegensatz zu den Listen der zehn sichersten Bezirke 2014 hinsichtlich der anderen beiden Kategorien ist hier\nzwischen Platz 5 und 6 kein so grosser Sprung zu erkennen.");
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
                Main.stage.setScene(Master.getInstance().getMenu_26());
            }
        });
        zurueck.setOnAction(new EventHandler<ActionEvent>()  {
            public void handle(ActionEvent event ) {
                Main.stage.setScene(Master.getInstance().getMenu_24());
            }
        });


    }

}
