import pycaw

# Get the default audio device
devices = pycaw.AudioUtilities.GetSpeakers()
device = pycaw.AudioUtilities.GetSpeaker(0)

# Set the volume to maximum
device.SetVolume(100)
