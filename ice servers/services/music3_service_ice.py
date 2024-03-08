import Ice
import os
import Music3

class MusicService3I(Music3.MusicService3):
    MUSIC_DIR = 'C:\\Users\\Ibrahim\\Desktop\\Music\\coldplay\\X&Y'
    CHUNK_SIZE = 1024 *1024 # 1MB

    def __init__(self):
        self.current_position = 0
        self.stopped = False

    def play(self, fileName, current=None):
        file_path = os.path.join(self.MUSIC_DIR, fileName)
        print(f"Playing {file_path}...")
        chunks = self.split_music_file(file_path)
        byte_sequence = bytes().join(chunks)
        print(byte_sequence)
        return byte_sequence

    def stop(self, current=None):
        self.stopped = True  

    def split_music_file(self, file_path):
        chunks = []
        try:
            with open(file_path, "rb") as f:
                i =0
                while True:
                    chunk = f.read(self.CHUNK_SIZE)
                    if not chunk:  # End of file reached
                        break
                    chunks.append(chunk)
                    i += 1
                    print(f"Chunk {i} read: {len(chunk)} bytes")
        except Exception as e:
            print("Error reading music file:", e)
        return chunks
    
    def storeMusicFile(self, fileData, fileName, current=None):
        file_path = os.path.join(self.MUSIC_DIR, fileName)
        try:
            with open(file_path, "wb") as f:
                f.write(fileData)
            print(f"Music file {fileName} stored successfully.")
        except Exception as e:
            print("Error storing music file:", e)

    def deleteMusicFile(self, file_name, current=None):
        file_path = os.path.join(self.MUSIC_DIR, file_name+".mp3")
        try:
            os.remove(file_path)
            print(f"File {file_name} deleted successfully.")
            return True
        except OSError as e:
            print(f"Error deleting file {file_name}: {e}")
            return False



