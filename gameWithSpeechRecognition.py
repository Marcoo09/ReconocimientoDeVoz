import random
import time
import speech_recognition as sr 


def recognize_speech_from_mic(recognizer, microphone):
		"""Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """

    # check that recognizer and microphone arguments are appropiate type
if not isinstance(recognizer,sr.Recognizer):
	raise TypeError("recognizer must be Recognizer instance")

if not isinstance(microphone, sr.microphone):
	raise TypeError("microphone must be Microphone instance")

    #adjust ambient to recognizer
with microphone as source:
	recognizer.adjust_for_ambient_noise(source)
    audio=recognizer.listen(source)

    #set up the response
response = {
	"success": True,
    "error":None,
    "transcription": None
	}	

    #try recognizing the seppech in the recording
    #if a request error or UnknownValueErro exceptionis caugth
    # update the respnse object accordingly
	
try:
	response["transcription"] = recognizer.recognize_google(audio)
except sr.RequestError:
		#API was unrachable or unresponsive
	response["success"] = False
	response["error"] = "Api unvailable"
except sr.UnknownValueErro:
		#speech was unintelligible
	response["error"] = "Unable to recognize speech"

return response

if __name__ == "main":
	#Set the list of words, maxnumber of guesses, adn prompt limit
	WORDS - ["apple","banana","grape","orange","mango"]
	NUM_GUESSES = 3
	PROMPT_LIMIT = 5

	#create recognizer and mic instances
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()

	#get a random word from tge list
	word = random.choice(WORDS)

	#format tge instruction String
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    #show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
		# get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times    	
        for j in range(PROMPT_LIMIT):
        	print('Gues {}. Speack!'.format(i + 1))
        	guess = recognize_speech_from_mic(recognizer, microphone)
			if guess["transcription"]:
				break
			if not guess["success"]:
				break
			print("I didnt catch that. What did you say?")        	

	#if the was an error, stop the game
	if guess["error"]:
		print("Error {}.".format(guess["error"]))
		break

	#show te user the transcription
	print("You said: {}".format(guess["transcription"]))

	#determine if guess is correct and if any attemps remain
	guess_is_correct = guess["transcription"].lower() == word.lower()
	user_has_more_attemps = i < NUM_GUESSES - 1

	#determine if the user has won the game
	#if not, repeat the loop if user has more attemps
	#if no attemps left, the user loses the game
	if guess_is_correct:
		print("Correct! You win!".format(word))
		break
	elif user_has_more_attemps:
		print("Incorrect. Try again \n")
	else:
		print("Sorry, you lose! \nI was thinking of '{}'".format(word))		

			
			