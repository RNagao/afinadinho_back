import wave

def freq_analysis(sound_wav):
    f = wave.open(sound_wav, 'rb')
    params = f.getparams()
    freq = f.getframerate()
    f.close()
    return freq


sound = "./notes_files/316902__jaz-the-man-2__la.wav"
print(freq_analysis(sound))