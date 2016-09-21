package sample;


public class Master {

    private static Master instance;

    private Menu menu;
    private Menu_1 menu_1;
    private Menu_2 menu_2;

    public static Master getInstance(){
        if(instance == null){
            instance = new Master();
        }
        return instance;
    }

    public Menu getMenu() {
        return menu;
    }
    public void setMenu(Menu menu) {
        this.menu = menu;
    }


    public Menu_1 getMenu_1() {
        return menu_1;
    }
    public void setMenu_1(Menu_1 menu_1) {
        this.menu_1 = menu_1;
    }


    public Menu_2 getMenu_2() {
        return menu_2;
    }
    public void setMenu_2(Menu_2 menu_2) {
        this.menu_2 = menu_2;
    }

}
