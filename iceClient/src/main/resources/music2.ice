module Music2 {
    struct MusicData {
        int id;
        string title;
        string artist;
        string filePath;
    };

    sequence<MusicData> MusicDataSeq;

    interface MusicService2 {
        MusicDataSeq getAll();
        MusicData getById(int id);
        MusicDataSeq searchByArtist(string artist);
        MusicDataSeq searchByTitle(string title);
    };
};
