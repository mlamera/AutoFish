from time import sleep, time
import pyautogui
import soundcard as sc
import sys
import numpy as np
import datetime


CAST_KEY = "-"
CATCH_KEY = "="
SOUND_THRESHOLD = 0.0008

# default 30 mins
MINUTES_TO_FISH = 30
SET_SPEAKER_ID = None
SEC = 1
SAMPLE_RATE = 48000
WAIT_PARAMETER = 2

def getSound(i):
    speaker_id = sc.default_speaker().name if SET_SPEAKER_ID == None else SET_SPEAKER_ID
    try:
        # Get microphone using speaker ID and allow recording of speakers output.
        with sc.get_microphone(id = speaker_id, include_loopback=True).recorder(samplerate = SAMPLE_RATE) as mic:
            # Record audio
            # numframes - number of frames to record (48000 * 1 = 48000 frames)
            # data is a numpy array of recorded audio data
            data = mic.record(numframes = SAMPLE_RATE * SEC)
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
    caught_fish = True if mean > SOUND_THRESHOLD else False
    print(f"{i} - catch = {caught_fish}: fish volume = {mean:9.5f}, speaker = '{speaker_id}'")

    return caught_fish


def wait():
    wait_time = np.random.exponential(WAIT_PARAMETER)
    print(f"Waiting for {wait_time:.3f} seconds ... ")
    sleep(wait_time)

def fish(mins):
    """
    1. Set timer
    2. Check if WoW window selected
    3. Start fishing
    4. If sound catch fish and cast again, else ignore (timer for loot ~0.5 secs)
    5. Timer on casting If no sound by time recast press "-" (timer for -recast)
    """




    input("Prepare to select Wow window. Press Enter to start.")
    print("Select WoW window. Starting fishing in...")
    for i in range (1, 6):
        sleep(1)
        print(i)
    start_time = time()
    counter = 0

    is_time_remaining = True
    while is_time_remaining:
        calculate = int(time() - start_time)
        time_left = str(datetime.timedelta(seconds=calculate))
        is_time_remaining = (calculate / 60) < mins
        print("\n")
        print("-" * 10)
        print(f"Fish iteration = {counter}, Time Elapsed = {time_left}, Minutes Selected = {mins}")
        pyautogui.press(CAST_KEY)

        for i in range(11):
            fish_sound = getSound(i)
            if fish_sound:
                pyautogui.press(CATCH_KEY)
                sleep(0.5)
                print("Fish caught!!!")
                wait()
                break
            sleep(0.8)
        counter += 1
    print(f"Finished fishing. {counter} fish caught!")


def main():
    while True:
        try:
            MINUTES_TO_FISH = int(input("Enter minutes to fish: "))
            if (MINUTES_TO_FISH < 1) :
                print("Number cannot be zero or negative.")
                continue
            else:
                break
        except ValueError:
            print("Please enter integers only.")
            continue

    fish(MINUTES_TO_FISH)

main()
