package com.ceri.iceclient;

import com.ceri.iceclient.Music1.MusicServicePrx;
import com.ceri.iceclient.Music2.MusicService2Prx;
import com.ceri.iceclient.Music2.MusicData;
import com.ceri.iceclient.Music3.MusicService3Prx;
import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.InitializationData;
import com.zeroc.Ice.ObjectPrx;
import com.zeroc.Ice.Util;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MusicServiceClient {
    private static MusicServiceClient instance;
    private Communicator communicator;
    private MusicServicePrx musicService1Proxy;
    private MusicService2Prx musicService2Proxy;
    private MusicService3Prx musicService3Proxy;
    private Process process;

    private MusicServiceClient() {
        InitializationData initData = new InitializationData();
        initData.properties = Util.createProperties();
        initData.properties.setProperty("Ice.MessageSizeMax", "10000000");

        communicator = Util.initialize(initData);

        // Initialize proxy for Music1 service
        ObjectPrx base1 = communicator.stringToProxy("Music1Service:default -p 10000");
        musicService1Proxy = MusicServicePrx.checkedCast(base1);
        if (musicService1Proxy == null) {
            throw new Error("Invalid proxy for Music1Service");
        }
        System.out.println("Connected to Music1Service successfully.");

        // Initialize proxy for Music2 service
        ObjectPrx base2 = communicator.stringToProxy("Music2Service:default -p 10001");
        musicService2Proxy = MusicService2Prx.checkedCast(base2);
        if (musicService2Proxy == null) {
            throw new Error("Invalid proxy for Music2Service");
        }
        System.out.println("Connected to Music2Service successfully.");

        // Initialize proxy for Music3 service
        ObjectPrx base3 = communicator.stringToProxy("Music3Service:default -p 10002");
        musicService3Proxy = MusicService3Prx.checkedCast(base3);
        if (musicService3Proxy == null) {
            throw new Error("Invalid proxy for Music3Service");
        }
        System.out.println("Connected to Music3Service successfully.");
    }

    // Get singleton instance
    public static synchronized MusicServiceClient getInstance() {
        if (instance == null) {
            instance = new MusicServiceClient();
        }
        return instance;
    }
    public boolean addMusic1(String title, String artist, String filePath) {
        boolean addedToDatabase = musicService1Proxy.createMusic(title, artist, title + ".mp3");

        if (addedToDatabase) {
            sendMusicFileToVLC(filePath);
        }

        return addedToDatabase;
    }


    public boolean updateMusic1(int id, String title, String artist, String filePath) {
        return musicService1Proxy.updateMusic(id, title, artist, filePath);
    }


    public boolean deleteMusic1(int id) {
        return musicService1Proxy.deleteMusic(id);
    }

    // Get all music from Music2 service
    public List<MusicData> getAllMusic2() {
        MusicData[] musicArray = musicService2Proxy.getAll();
        return new ArrayList<>(Arrays.asList(musicArray));
    }

    public MusicData getMusicById2(int id) {
        try {
            return musicService2Proxy.getById(id);
        } catch (Exception e) {
            return null;
        }
    }

    public List<MusicData> searchMusicByArtist2(String artist) {
        try {
            MusicData[] musicArray = musicService2Proxy.searchByArtist(artist);
            return new ArrayList<>(Arrays.asList(musicArray));
        } catch (Exception e) {
            return null;
        }
    }

    public List<MusicData> searchMusicByTitle2(String title) {
        MusicData[] musicArray = musicService2Proxy.searchByTitle(title);
        return new ArrayList<>(Arrays.asList(musicArray));
    }

    public List<byte[]> playMusic3(String fileName) {
        return Collections.singletonList(musicService3Proxy.play(fileName));
    }

    public void saveMusicDataToFile(List<byte[]> musicChunks, String fileName) {
        try (FileOutputStream fos = new FileOutputStream(fileName)) {
            for (byte[] chunk : musicChunks) {
                fos.write(chunk);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public void play(String fileName) {
        fileName = fileName + ".mp3";
        List<byte[]> musicChunks = playMusic3(fileName);

        String tempFileName = "temp_music.mp3";
        saveMusicDataToFile(musicChunks, tempFileName);

        System.out.println("Playing music...");
        new Thread(() -> {
            playMusicWithVLC(tempFileName);
        }).start();
    }

    public void playMusicWithVLC(String fileName) {
        try {
            File file = new File(fileName);
            if (!file.exists()) {
                System.err.println("File does not exist: " + fileName);
                return;
            }

            System.out.println("Trying to play file: " + fileName);

            ProcessBuilder pb = new ProcessBuilder("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe", file.getAbsolutePath());
            pb.redirectErrorStream(true);
            process = pb.start();

            // Read and log output of VLC process
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }

            System.out.println("VLC process started.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void pause() {
        try {
            // Check if VLC process is running
            if (process != null && process.isAlive()) {
                // Suspend the VLC process
                process.pid();


                System.out.println("Music paused.");
            } else {
                System.out.println("VLC process is not running.");
            }

        } catch (UnsupportedOperationException e) {
            System.err.println("Pausing is not supported on this platform.");
        }
    }

    public void stop() {
        try {
            // Check if VLC process is running
            if (process != null && process.isAlive()) {
                // Kill the VLC process
                process.destroy();

                System.out.println("Music stopped.");
            } else {
                System.out.println("VLC process is not running.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    // Add a method to send music file to the VLC server
    public boolean sendMusicFileToVLC(String filePath) {
        try {
            // Read the music file as bytes
            File file = new File(filePath);
            byte[] fileData = new byte[(int) file.length()];
            FileInputStream fis = new FileInputStream(file);
            fis.read(fileData);
            fis.close();

            // Call the VLC server method to store the music file
            musicService3Proxy.storeMusicFile(fileData, file.getName());
            System.out.println("Music file sent to VLC server successfully.");
            return true;
        } catch (IOException e) {
            System.err.println("Error sending music file to VLC server: " + e.getMessage());
            return false;
        }
    }

    public void deleteMusicFileFromVLC(String fileName) {
        musicService3Proxy.deleteMusicFile(fileName);
    }


    // Shutdown ICE communicator
    public void shutdown() {
        if (communicator != null) {
            communicator.destroy();
            System.out.println("ICE communicator shut down successfully.");
        }
    }
}
