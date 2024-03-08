module Music1 {
    interface MusicService {
        bool createMusic(string title, string artist, string filePath);
        bool updateMusic(int id, string title, string artist, string filePath);
        bool deleteMusic(int id);
    };
};
