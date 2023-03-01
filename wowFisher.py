from . import config
import pyautogui
import soundcard as sc
import sys
import numpy as np



def getSound():
    speaker_id = sc.default_speaker().name if config.SPEAKER_ID == None else config.SPEAKER_ID
    try:
        # Get microphone using speaker ID and allow recording of speakers output.
        with sc.get_microphone(id = speaker_id, include_loopback=True).recorder(samplerate = config.SAMPLE_RATE) as mic:
            # Record audio
            # numframes - number of frames to record (48000 * 1 = 48000 frames)
            # data is a numpy array of recorded audio data
            data = mic.record(numframes = config.SAMPLE_RATE * config.SEC)
    # Lists available speakers if none found.
    except IndexError:
        print(f"Couldn't find speaker device '{speaker_id}'. Available options are:")
        for speaker in sc.all_speakers():
            print(speaker.name)
        print("Set 'SPEAKER_ID' to one of the speakers listed above")
        sys.exit(1)

    # No idea what this means...
    mean = sum(np.absolute(data)) / len(data)
    mean = mean[0]
    caught_fish = True if mean > config.SOUND_THRESHOLD else False
    print(f"{i} catch = {caught_fish}: fish volume = {mean:9.5f}, speaker = '{speaker_id}'")

    return caught_fish


def wait():
    return 0

def main():
    """
    1. Set timer
    2. Check if WoW window selected
    3. Start fishing
    4. If sound catch fish and cast again, else ignore (timer between caught and cast ~0.5 secs)
    5. Timer on casting If no sound by time recast press "-" (timer for recast)

    """
    return 0

main()
