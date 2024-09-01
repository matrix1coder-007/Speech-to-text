import pyttsx3

sample_test = 'Hi! How are you? I am fine. Hope you are doing good too!'

# ----------------------------------------------------------------------------------------
# initialization -- Sample-00
# ----------------------------------------------------------------------------------------

speech_to_text_engine = pyttsx3.init()
speech_to_text_engine.say(sample_test)
speech_to_text_engine.runAndWait()


# ----------------------------------------------------------------------------------------
# change voice, rate, volume -- Sample-01
# ----------------------------------------------------------------------------------------

# Rate
initial_rate = speech_to_text_engine.getProperty('rate')
print('initial rate', initial_rate)
altered_rate = initial_rate*(100)
speech_to_text_engine.setProperty(sample_test, altered_rate)
print('altered rate', speech_to_text_engine.getProperty('rate'))

speech_to_text_engine.say('After change in rate' + sample_test)

# ----------------------------------------------------------------------------------------

# Volume
initial_volume = speech_to_text_engine.getProperty('volume')
altered_volume = (200)*initial_volume
speech_to_text_engine.setProperty(sample_test, altered_volume)

speech_to_text_engine.say('After change in volume' + sample_test)

# ----------------------------------------------------------------------------------------

# Voice: male component idx = 0; female component idx = 1
initial_voice = speech_to_text_engine.getProperty('voices')

male_volume_idx = initial_voice[0].id
print(initial_voice[0])
speech_to_text_engine.setProperty(sample_test, (300)*male_volume_idx)
speech_to_text_engine.say('After change in male component voice' + sample_test)

female_volume_idx = initial_voice[1].id
print(initial_voice[1])
speech_to_text_engine.say('After change in female component voice' + sample_test)

# ----------------------------------------------------------------------------------------

speech_to_text_engine.say(sample_test)
speech_to_text_engine.runAndWait()
speech_to_text_engine.stop()

# Saving voice to a file
speech_to_text_engine.save_to_file(sample_test, 'sample_test.mp3')
speech_to_text_engine.runAndWait()

# ----------------------------------------------------------------------------------------
