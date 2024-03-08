package com.ceri.iceclient;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;


public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 720, 740);
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();


    }



    public static void main(String[] args) {
 /*       // ICE communication after launching JavaFX application
        // Initialize the ICE client
        MusicServiceClient musicServiceClient = new MusicServiceClient();

        // Test ICE communication
        // For example, get all music from Music2 service
        List<MusicData> allMusic = musicServiceClient.getAllMusic2();
        List<MusicData> musicByArtist = musicServiceClient.searchMusicByArtist2("Queen");
        System.out.println("All Music from Music2 service:");
        for (MusicData musicData : allMusic) {
            System.out.println(musicData.title);
        }
        System.out.println("Music by Queen from Music2 service:");
        for (MusicData musicData : musicByArtist) {
            System.out.println(musicData.title);
        }

        // test addMusic1
        //musicServiceClient.addMusic1("test", "test", "C:\\Users\\josep\\Music\\Queen\\test");
        //System.out.println("Music added to Music1 service");
        // find the id of the music added with seachMusicByTitle2
        List<MusicData> musicByTitle = musicServiceClient.searchMusicByTitle2("test");
        int id = -1;
        for (MusicData musicData : musicByTitle) {
            if (musicData.title.equals("test")) {
                id = musicData.id;
                break;
            }
        }
        System.out.println("id: " + id);


         musicServiceClient.updateMusic1( id,"testUpdate", "test", "C:\\Users\\josep\\Music\\Queen\\test");
        System.out.println("Music updated in Music1 service");

        // test deleteMusic1
        //musicServiceClient.deleteMusic1(id);
        //System.out.println("Music deleted from Music1 service");

        // Call playMusic3 method only once

        musicServiceClient.shutdown();*/
        //MusicServiceClient musicServiceClient = MusicServiceClient.getInstance();
        //musicServiceClient.addMusic1("test", "test", "C:\\Users\\josep\\Music\\Queen\\test");
        launch();
    }
}
