module Music3 {
    sequence<byte> ByteSeq;

    interface MusicService3 {
        ByteSeq play(string fileName);
        void stop();
        void storeMusicFile(ByteSeq fileData, string fileName);
        void deleteMusicFile(string fileName);
    }
};
