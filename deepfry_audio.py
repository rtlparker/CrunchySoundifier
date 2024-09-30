from pydub import AudioSegment
import argparse

def deepfry_audio(input_file, output_file, quality_level="Low", volume_level="Normal"):
    quality_settings = {
        "Low": {"sample_width": 1, "channels": 1, "frame_rate": 8000},
        "Funny": {"sample_width": 1, "channels": 1, "frame_rate": 4000},
        "Dumpster": {"sample_width": 1, "channels": 1, "frame_rate": 3500},
        "No": {"sample_width": 1, "channels": 1, "frame_rate": 1200}
    }

    volume_adjustments = {
        "Loud": 10,
        "Quiet": -10,
        "Normalized": "normalize",
        "Normal": 0
    }

    try:
        audio = AudioSegment.from_file(input_file)

        # Apply quality settings
        if quality_level in quality_settings:
            settings = quality_settings[quality_level]
            audio = (audio.set_sample_width(settings["sample_width"])
                          .set_channels(settings["channels"])
                          .set_frame_rate(settings["frame_rate"]))
        else:
            print(f"Invalid quality level '{quality_level}'. Available options: {', '.join(quality_settings.keys())}")
            return

        # Apply volume adjustments
        if volume_level in volume_adjustments:
            adjustment = volume_adjustments[volume_level]
            if adjustment == "normalize":
                audio = audio.normalize(headroom=1.0)
            else:
                audio += adjustment  # Adjust volume
        else:
            print(f"Invalid volume level '{volume_level}'. Available options: {', '.join(volume_adjustments.keys())}")
            return

        # Export the processed audio
        audio.export(output_file, format="wav")
        print(f"Conversion complete. Quality: {quality_level}, Volume: {volume_level}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Deep fry an audio file by degrading its quality and adjusting volume.'
    )
    parser.add_argument('input_file', help='Input audio file (e.g., input.mp3)')
    parser.add_argument('output_file', help='Output audio file (e.g., output.wav)')
    parser.add_argument(
        'quality_level',
        nargs='?',
        default='Low',
        choices=['Low', 'Funny', 'Dumpster', 'No'],
        help='Quality level: Low, Funny, Dumpster, No'
    )
    parser.add_argument(
        'volume_level',
        nargs='?',
        default='Normal',
        choices=['Loud', 'Quiet', 'Normalized', 'Normal'],
        help='Volume level: Loud, Quiet, Normalized, Normal'
    )

    args = parser.parse_args()
    deepfry_audio(args.input_file, args.output_file, args.quality_level, args.volume_level)

if __name__ == "__main__":
    main()
