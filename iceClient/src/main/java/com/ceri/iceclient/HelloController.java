package com.ceri.iceclient;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import com.ceri.iceclient.Music2.MusicData;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.List;

public class HelloController {
    @FXML
    public TextField titleSearchField;

    @FXML
    private TextField artistSearchField;

    @FXML
    private ListView<MusicData> musicListView;

    private MusicServiceClient musicServiceClient;

    // Use the singleton instance of MusicServiceClient
    public HelloController() {
        musicServiceClient = MusicServiceClient.getInstance();
    }

    @FXML
    protected void searchByArtist() {
        String artist = artistSearchField.getText();
        List<MusicData> searchResults = musicServiceClient.searchMusicByArtist2(artist);
        displaySearchResults(searchResults);
    }

    @FXML
    protected void searchByTitle() {
        String name = titleSearchField.getText();
        List<MusicData> searchResults = musicServiceClient.searchMusicByTitle2(name);
        displaySearchResults(searchResults);
    }

    private void displaySearchResults(List<MusicData> searchResults) {
        musicListView.getItems().clear();
        if (searchResults != null) {
            musicListView.getItems().addAll(searchResults);
        } else {
            // Handle case where search results are null (e.g., service error)
            System.out.println("Error retrieving search results.");
        }
    }

    @FXML
    private void openAddMusicForm(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("add-music.fxml"));
        Parent root = loader.load();
        Stage stage = new Stage();
        stage.setScene(new Scene(root));
        stage.show();
    }

    @FXML
    public void playMusic(String title) {
        musicServiceClient.play(title);
    }

    @FXML
    public void pauseMusic(String title) {
        musicServiceClient.pause();
    }

    @FXML
    public void stopMusic(String title) {
        musicServiceClient.stop();
    }

    @FXML
    public void deleteMusic(int id) {
        musicServiceClient.deleteMusic1(id);
    }

    @FXML
    void deleteMusicFromVLC(String title) {
        musicServiceClient.deleteMusicFileFromVLC(title);
    }
}
