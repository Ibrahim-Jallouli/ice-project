package com.ceri.iceclient;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;

public class AddMusic {
    @FXML
    private TextField titleField;

    @FXML
    private TextField artistField;

    @FXML
    private Label fileNameLabel;

    private MusicServiceClient musicServiceClient;

    private File selectedFile; // Declaring selectedFile outside the uploadMusic method

    public AddMusic() {
        // Initialize MusicServiceClient
        musicServiceClient = MusicServiceClient.getInstance();
    }

    @FXML
    private void uploadMusic(ActionEvent event) {
        // Open file chooser dialog
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Select Music File");
        selectedFile = fileChooser.showOpenDialog(new Stage());

        if (selectedFile != null) {
            // Set the file name to the Label
            fileNameLabel.setText(selectedFile.getName());
        }
    }


    @FXML
    private void addMusic(ActionEvent event) {
        // Retrieve entered title and artist
        String title = titleField.getText();
        String artist = artistField.getText();
        System.out.println(selectedFile.getName());
        // Check if title and artist are not empty
        if (!title.isEmpty() && !artist.isEmpty() && selectedFile != null) { // Check if selectedFile is not null
            // Upload the music file
            boolean addedToDatabase = musicServiceClient.addMusic1(title, artist, selectedFile.getAbsolutePath());

            if (addedToDatabase) {
                System.out.println("Music added to the database successfully.");
            } else {
                System.out.println("Error adding music to the database.");
            }
        } else {
            System.out.println("Title, artist, or music file cannot be empty.");
        }
    }
}
