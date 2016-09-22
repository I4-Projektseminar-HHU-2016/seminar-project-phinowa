package sample;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.HPos;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;


public class Menu extends Scene{

    private Button start;
    private Button exit;
    private Label label_ueberschrift;
    private Label label_text;

    GridPane grid;
    int width, height;

    Master master;

    public Menu(GridPane grid, int width, int height){
        super(grid,width,height);
        this.grid = grid;
        this.width = width;
        this.height = height;
        this.label_ueberschrift = new Label("Verbrechen in Baltimore");
        this.label_text = new Label("Eine Auswertung von Philipp Nowak.");
        this.start = new Button("Start");
        this.exit = new Button("Beenden");
        this.master = Master.getInstance();

        //ID fuer Hintergrundbild, das in CSS-Datei eingelesen wird
        grid.setId("start_menu_box");
        //ID fuer Ueberschrift, die in CSS-Datei eingelesen wird
        label_ueberschrift.setId("ueberschrift_start_menu");

        //Ordnen von Komponenten (Layout) bei Menue
        grid.setVgap(10);                     //Platz vertikal zwischen Komponenten lassen.
        grid.setHalignment(start, HPos.CENTER);
        grid.setHalignment(exit, HPos.RIGHT);
        grid.setPadding(new Insets(30, 50, 50, 300));   //Abstand der GUI-Komponenten zur GridPane
        grid.add(label_ueberschrift, 0, 0);             //GUI-Komponente, Zeile, Spalte...
        grid.add(label_text, 0, 1);
        grid.add(start, 0, 8);
        grid.add(exit, 0, 8);
        grid.setGridLinesVisible(false); //true: zur Selbstueberpruefung der Linien

        this.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm()); //Zugriff auf CSS-Datei


        //Registrierung von Listenern
        this.start.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.setScene(Master.getInstance().getMenu_einleitung());
            }
        });
        this.exit.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Main.stage.close();
            }
        });
    }
}
