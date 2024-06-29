import os
import librosa

# Define the folder path containing the audio files
folder_path = 'path/to/your/folder'

# Define the duration threshold in seconds
duration_threshold = 3.0

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is an audio file by its extension
    if file_path.endswith(('.mp3', '.wav', '.flac', '.ogg', '.m4a')):
        try:
            # Load the audio file
            y, sr = librosa.load(file_path, sr=None)
            
            # Calculate the duration of the audio file
            duration = librosa.get_duration(y=y, sr=sr)
            
            # Check if the duration exceeds the threshold
            if duration > duration_threshold:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path} (Duration: {duration:.2f} seconds)")
        
        except Exception as e:
            pass

print("Processing complete.")
