module com.ceri.iceclient {
    requires javafx.controls;
    requires javafx.fxml;
    requires com.zeroc.ice;


    opens com.ceri.iceclient to javafx.fxml;
    exports com.ceri.iceclient;
    exports com.ceri.iceclient.Music1;
    exports com.ceri.iceclient.Music2;
    exports com.ceri.iceclient.Music3;
}
