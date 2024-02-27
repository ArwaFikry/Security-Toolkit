import wave
import os

def hide_data_in_audio(original_audio_path, message,enc_key):
    output_audio_path = original_audio_path[:original_audio_path.find(".")] + "steg" + original_audio_path[original_audio_path.find("."):]
    audio = wave.open(original_audio_path, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    # Add a delimiter to mark the end of the message
    message += '###'

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Embed the message in the audio using LSB
    for i, bit in enumerate(binary_message):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bit)

    frames_modified = bytes(frame_bytes)

    # Write the modified frames to a new audio file
    with wave.open(output_audio_path, 'wb') as modified_audio:
        modified_audio.setparams(audio.getparams())
        modified_audio.writeframes(frames_modified)

    audio.close()
    modified_audio.close()

def reveal_data_from_audio(audio_path,enc_key):
    audio = wave.open(audio_path, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    # Extract LSBs
    ls_bits = [frame_byte & 1 for frame_byte in frame_bytes]

    # Convert LSBs to characters
    binary_message = ''.join(map(str, ls_bits))

    # Split binary_message using the delimiter
    message = ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)])
    message = message.split('###')[0]

    # Remove padding characters
    message = message.rstrip('#')


    audio.close()
    return message

# Get user input for operation choice


# Hide data in audio
# hide_data_in_audio(original_audio_path, output_audio_path, message_to_hide)



    # Reveal data from audio
# reveal_data_from_audio(audio_path)
