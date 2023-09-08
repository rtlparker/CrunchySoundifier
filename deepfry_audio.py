from pydub import AudioSegment
import random
import sys

def deepfry_audio(input_file, output_file, quality_level="Low", volume_level="Normal"):
    try:
        audio = AudioSegment.from_mp3(input_file)

        if quality_level == "Low":
            # Low-quality settings (current settings)
            audio = audio.set_sample_width(1)  # Reduce the sample width to 8-bit
            audio = audio.set_channels(1)  # Convert to mono audio
            audio = audio.set_frame_rate(8000)  # Reduce the sample rate
        elif quality_level == "Funny":
            # Funny quality settings (lower quality)
            audio = audio.set_sample_width(1)  # Reduce the sample width to 8-bit
            audio = audio.set_channels(1)  # Convert to mono audio
            audio = audio.set_frame_rate(4000)  # Further reduce the sample rate
        elif quality_level == "Dumpster":
            # Dumpster quality settings (slightly below "Funny")
            audio = audio.set_sample_width(1)  # Reduce the sample width to 8-bit
            audio = audio.set_channels(1)  # Convert to mono audio
            audio = audio.set_frame_rate(3500)  # Slightly lower sample rate
        elif quality_level == "No":
            # No quality settings (much worse than the others)
            audio = audio.set_sample_width(1)  # Reduce the sample width to 8-bit
            audio = audio.set_channels(1)  # Convert to mono audio
            audio = audio.set_frame_rate(1200)  # Much lower sample rate
        else:
            print("Invalid quality level. Please choose from: Low, Funny, Dumpster, No")
            return

        if volume_level == "Loud":
            audio = audio + 10  # Increase the volume
        elif volume_level == "Quiet":
            audio = audio - 10  # Decrease the volume
        elif volume_level == "Normalized":
            # Match the original file's volume
            target_dBFS = audio.dBFS - audio.max_dBFS
            audio = audio + target_dBFS

        # Export the deepfried audio
        audio.export(output_file, format="wav")

        print(f"{quality_level} audio conversion complete. Volume: {volume_level}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python deepfry_audio.py input.mp3 output.wav quality_level volume_level")
        print("Available quality levels: Low, Funny, Dumpster, No")
        print("Available volume levels: Loud, Normalized, Quiet")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        quality_level = sys.argv[3]
        volume_level = sys.argv[4]
        deepfry_audio(input_file, output_file, quality_level, volume_level)
