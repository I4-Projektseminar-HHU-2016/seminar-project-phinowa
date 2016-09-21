package sample;


import javafx.application.Application;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class Main extends Application {

    public static int width = 1000;
    public static int height = 600;

    public static Stage stage;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start (Stage primaryStage) throws Exception {
        stage = primaryStage;
        initialize();
        primaryStage.setTitle("Projektseminar I4 - Philipp Nowak - Verbrechen in Baltimore");    //Titel des Fensters
        stage.setScene(Master.getInstance().getMenu());
        primaryStage.setResizable(false);   //Fenstergroesse kann nicht veraendert werden
        primaryStage.show();   //Fenster zeigen
    }

    private void initialize(){
        Master master = Master.getInstance();
        master.setMenu(new Menu(new VBox(), width, height));
        master.setMenu_1(new Menu_1(new VBox(), width, height));
        master.setMenu_2(new Menu_2(new VBox(), width, height));
    }
}