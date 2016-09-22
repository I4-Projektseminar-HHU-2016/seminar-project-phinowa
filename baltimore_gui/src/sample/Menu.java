package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.*;


public class Menu extends Scene{

    private Button start;
    private Button exit;
    private Label label_ueberschrift;
    private Label label_text;

    VBox box;
    int width, height;

    Master master;

    public Menu(VBox box, int width, int height){
        super(box,width,height);
        this.box = box;
        this.width = width;
        this.height = height;
        this.label_ueberschrift = new Label("Ueberschrift!");
        this.label_text = new Label("Test.\nTest.\nTest.");
        this.start = new Button("Start");
        this.exit = new Button("Beenden");
        this.master = Master.getInstance();

        //ID fuer Hintergrundbild, das in CSS-Datei eingelesen wird
        box.setId("start_menu_box");

        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(10, 50, 50, 50)); //Abstand der GUI-Komponenten zum Rand
        box.setSpacing(15);
        box.getChildren().addAll(label_ueberschrift, label_text, start, exit);

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.start.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu_1());
            }
        });
        this.exit.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.close();
            }
        });
    }
}
