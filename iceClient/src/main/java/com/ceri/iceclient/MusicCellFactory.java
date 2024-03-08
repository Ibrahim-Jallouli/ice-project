package com.ceri.iceclient;

import com.ceri.iceclient.Music2.MusicData;
import javafx.scene.control.Button;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.layout.HBox;
import javafx.util.Callback;

public class MusicCellFactory implements Callback<ListView<MusicData>, ListCell<MusicData>> {

    HelloController helloController = new HelloController();

    @Override
    public ListCell<MusicData> call(ListView<MusicData> listView) {
        return new ListCell<>() {
            private final Button playButton = new Button("Play");
            private final Button stopButton = new Button("Stop");
            private final Button pauseButton = new Button("Pause");
            private final Button deleteButton = new Button("Delete");

            {
                // Initially disable the buttons
                playButton.setDisable(true);
                stopButton.setDisable(true);
                pauseButton.setDisable(true);
                deleteButton.setDisable(true);

                // Add event handlers to enable buttons on cell click
                this.setOnMouseClicked(event -> {
                    playButton.setDisable(false);
                    stopButton.setDisable(false);
                    pauseButton.setDisable(false);
                    deleteButton.setDisable(false);

                    // Retrieve and print the music title
                    MusicData item = getItem();
                    if (item != null) {
                        System.out.println("Clicked Music Title: " + item.title);
                    }
                });

                // Add event handler to play button
                playButton.setOnAction(event -> {
                    MusicData item = getItem();
                    if (item != null) {
                        helloController.playMusic(item.title);
                    }
                });
                pauseButton.setOnAction(event -> {
                    MusicData item = getItem();
                    if (item != null) {
                        helloController.pauseMusic(item.title);
                    }
                });
                stopButton.setOnAction(event -> {
                    MusicData item = getItem();
                    if (item != null) {
                        helloController.stopMusic(item.title);
                    }
                });
                deleteButton.setOnAction(event -> {
                    MusicData item = getItem();
                    if (item != null) {
                        // Call the deleteMusic1 method in HelloController

                        helloController.deleteMusic(item.id);
                        helloController.deleteMusicFromVLC(item.title);
                    }
                });
            }

            @Override
            protected void updateItem(MusicData item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setText(null);
                    setGraphic(null);
                } else {
                    setText(item.title);

                    // Add buttons to HBox
                    HBox buttonBox = new HBox(playButton, stopButton, pauseButton, deleteButton);
                    buttonBox.setSpacing(5); // Set spacing between buttons
                    buttonBox.setMaxWidth(Double.MAX_VALUE); // Allow buttons to expand horizontally
                    setGraphic(buttonBox);
                }
            }
        };
    }
}
