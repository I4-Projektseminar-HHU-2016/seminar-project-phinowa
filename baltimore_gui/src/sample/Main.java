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
        master.setMenu_3(new Menu_3(new VBox(), width, height));
        master.setMenu_4(new Menu_4(new VBox(), width, height));
        master.setMenu_5(new Menu_5(new VBox(), width, height));
        master.setMenu_6(new Menu_6(new VBox(), width, height));
        master.setMenu_7(new Menu_7(new VBox(), width, height));
        master.setMenu_8(new Menu_8(new VBox(), width, height));
        master.setMenu_9(new Menu_9(new VBox(), width, height));
        master.setMenu_10(new Menu_10(new VBox(), width, height));
        master.setMenu_11(new Menu_11(new VBox(), width, height));
        master.setMenu_12(new Menu_12(new VBox(), width, height));
        master.setMenu_13(new Menu_13(new VBox(), width, height));
        master.setMenu_14(new Menu_14(new VBox(), width, height));
        master.setMenu_15(new Menu_15(new VBox(), width, height));
        master.setMenu_16(new Menu_16(new VBox(), width, height));
        master.setMenu_17(new Menu_17(new VBox(), width, height));
        master.setMenu_18(new Menu_18(new VBox(), width, height));
        master.setMenu_19(new Menu_19(new VBox(), width, height));
        master.setMenu_20(new Menu_20(new VBox(), width, height));
        master.setMenu_21(new Menu_21(new VBox(), width, height));
        master.setMenu_22(new Menu_22(new VBox(), width, height));
        master.setMenu_23(new Menu_23(new VBox(), width, height));
        master.setMenu_24(new Menu_24(new VBox(), width, height));
        master.setMenu_25(new Menu_25(new VBox(), width, height));
        master.setMenu_26(new Menu_26(new VBox(), width, height));
        master.setMenu_27(new Menu_27(new VBox(), width, height));
        master.setMenu_28(new Menu_28(new VBox(), width, height));
        master.setMenu_29(new Menu_29(new VBox(), width, height));
        master.setMenu_30(new Menu_30(new VBox(), width, height));
    }
}
