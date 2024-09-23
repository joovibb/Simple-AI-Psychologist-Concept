

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import sounddevice
import pyaudio




def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You said: " + said)
        except Exception as e:
            print("Exception: " + str(e))
        
    return said

text = get_audio()
name = " "

Hlo = ["hello","hi","Doctor Merin"]
if any(word in text for word in Hlo):
    speak("hello i'm doctor Merin Thomas,how are you? what's your name....?" )
    name = get_audio()
    speak("Hi")
    speak(name)
    speak("How are you doing...? How can i help you tell me if you have any kind of psycological problem among these")
    print("""Depression – Persistent feelings of sadness, loss of interest, and a lack of motivation.
             Anxiety Disorders – Excessive fear or worry, including panic disorder, generalized anxiety disorder, and social anxiety.
             Obsessive-Compulsive Disorder (OCD) – Repeated, unwanted thoughts (obsessions) and repetitive behaviors (compulsions).
             Post-Traumatic Stress Disorder (PTSD) – Anxiety and flashbacks triggered by a traumatic event.
             Bipolar Disorder – Extreme mood swings between mania (high energy) and depression.
             Schizophrenia – A disorder involving distorted thinking, perceptions, and emotions.
             Personality Disorders – Long-term patterns of behavior and thoughts that deviate from cultural expectations (e.g., borderline personality disorder, narcissistic personality disorder).
             Eating Disorders – Disorders related to unhealthy eating habits, such as anorexia nervosa, bulimia nervosa, and binge-eating disorder.
             Attention-Deficit/Hyperactivity Disorder (ADHD) – Inability to focus, hyperactivity, and impulsiveness.
             Substance Use Disorders – Dependence on or addiction to substances like alcohol, drugs, or medication.
             Phobias – Intense, irrational fears of specific situations, objects, or activities.
             Dissociative Disorders – Involves a disconnection between thoughts, identity, consciousness, and memory (e.g., dissociative identity disorder).
             Autism Spectrum Disorder (ASD) – Impacts social interaction, communication, and behavior.
             Sleep Disorders – Problems related to sleep, such as insomnia, sleep apnea, and narcolepsy.
             Somatic Symptom Disorder – Excessive worry about physical symptoms like pain or fatigue, even when no medical condition is present.""")
    problem = get_audio()
    DiP = ["depression", "Dipression", "i'm having depression", "i am having depression", "having depression"]
    AnD = ["anxiety", "anxietydisorders", "i'm having anxiety", "i am having anxiety", "having anxiety"]
    PTSD = ["ptsd", "post traumatic stress disorder", "i'm having ptsd", "i am having ptsd", "having ptsd"]
    SUBSTANCE_USE = ["substance use", "drug abuse", "alcohol abuse", "i'm struggling with substance use", "having substance abuse"]
    PHOBIAS = ["phobia", "fear of", "i'm having a phobia", "i have a phobia", "having phobia"]
    SLEEP_DISORDER = ["sleep disorder", "insomnia", "i can't sleep", "i am having sleep problems", "having trouble sleeping"]


    if any(d in problem for d in DiP):  
           speak("Hey")
           speak(name)
           speak("""1. "Look, the most important thing is that you're not alone in this. Depression is real, and it's tough, but we have ways to help. Therapy, especially cognitive-behavioral therapy, can do wonders. It helps you understand those negative thoughts, the ones pulling you down, and teaches you how to challenge them. And sometimes, medication—like antidepressants—can assist too. It might take a little time to find what works best for you, but together, we can figure that out. Your health is a priority, and there are tools we can use to get you back on your feet."
           "One thing I always stress is self-care. Exercise, even something as simple as a walk, releases endorphins that naturally boost your mood. Sleep, too—creating a consistent routine can make a huge difference. And, of course, nutrition matters. Staying connected with friends or family helps fight that isolation depression often brings. It won't be easy, but healing is a process. Set small goals, maintain structure in your daily life, and take things one step at a time. And remember, if things ever feel too heavy or dark, you can always reach out—there's no shame in asking for help.".""")
           
           
    elif any(anxiety in problem for anxiety in AnD):
           speak("Hey")
           speak(name)
           speak("""
           First of all, I want you to know that what you're experiencing is completely valid, and there are solutions. One of the most effective treatments we use for anxiety is cognitive-behavioral therapy, or CBT. It helps you recognize those irrational fears and teaches techniques to relax and calm your mind. We can also try exposure therapy, which works by slowly helping you face the things that make you anxious, giving you control back. If necessary, medication like SSRIs can help as well, but it's important we monitor it closely and combine it with therapy for the best results.
           Now, in addition to therapy, there are self-care practices that make a big difference. Exercise is a natural anxiety reliever—just going for a walk or trying yoga can reduce stress. Mindfulness and meditation are also powerful tools, helping you stay grounded when your thoughts start spiraling. I also want you to focus on getting 7-9 hours of sleep each night; anxiety often disrupts sleep, and we need to stabilize that. A balanced diet, avoiding too much caffeine, sugar, and alcohol, can go a long way in improving your mental well-being.
           I also recommend using grounding techniques when anxiety peaks. One method is the '5-4-3-2-1' technique: look for five things you can see, four you can touch, three you can hear, two you can smell, and one you can taste. This helps bring your focus back to the present. It's important to stay connected too—talk to friends, family, or consider joining a support group. We can set small, achievable goals and maintain a consistent routine to give you structure and stability."
           Finally, be patient with yourself. Healing takes time, and progress is gradual. Celebrate your small victories, and remember, anxiety isn't a sign of weakness. You're stronger than you think, and you’re already on the right path. If it ever feels like too much, don’t hesitate to reach out to me or another professional. Help is always here when you need it.""")
    elif any(ptsd in problem for ptsd in PTSD):
           speak("Hey")
           speak(name)
           speak("""
           "PTSD is something a lot of people struggle with after experiencing a traumatic event. It’s important to remember that you’re not stuck in this—it is possible to heal. Therapy, especially trauma-focused cognitive-behavioral therapy (CBT) or Eye Movement Desensitization and Reprocessing (EMDR), can be really effective in processing those traumatic memories and reducing the stress they cause. You’re not reliving the trauma; we’ll be working on transforming how your brain reacts to it."
           "Self-care is crucial in managing PTSD. This means prioritizing rest, exercise, and relaxation techniques, like mindfulness or breathing exercises. Creating a safe space at home where you feel in control can help too. Stay connected with people who make you feel secure, and don’t hesitate to reach out for support when things feel overwhelming. If the symptoms ever feel too intense or like they’re taking over, medications like SSRIs can assist alongside therapy. Healing from PTSD can take time, but with the right tools and support, progress is not only possible but probable."
           """)

    elif any(substance in problem for substance in SUBSTANCE_USE):
           speak("Hey")
           speak(name)
           speak("""
           "Substance use is something that affects both your mind and body, but recovery is absolutely possible. The first step is recognizing the need for help, and you’ve already done that by sharing this with me. Therapy, like cognitive-behavioral therapy (CBT), is key in understanding what triggers the desire to use substances, whether it's drugs or alcohol, and how we can break that cycle."
           "It’s crucial to surround yourself with a support system, whether through friends, family, or a recovery group. We can also explore medically-assisted treatments if needed, especially if withdrawal is a concern. Focus on building healthy routines—exercise, balanced nutrition, and proper sleep all play a huge role in recovery. Relapses might happen, but don’t let that discourage you. Recovery is a journey, and every step counts."
           """)

    elif any(phobia in problem for phobia in PHOBIAS):
           speak("Hey")
           speak(name)
           speak("""
           "Phobias can feel overwhelming, but there are proven ways to manage and overcome them. Therapy, especially exposure therapy, can gradually help you face the thing you're afraid of, one small step at a time. We’ll work together to slowly and safely confront the phobia in a way that helps you regain control."
           "Breathing exercises, mindfulness, and grounding techniques can help calm your mind when anxiety spikes. If it ever becomes too intense, medications like beta-blockers or sedatives might help temporarily, but therapy is key in addressing the root of the fear."
           """)

    elif any(sleep in problem for sleep in SLEEP_DISORDER):
           speak("Hey")
           speak(name)
           speak("""
           "Sleep disorders can have a significant impact on your life, but they’re treatable. Cognitive-behavioral therapy for insomnia (CBT-I) is one of the best ways to address sleep problems. It works by changing the thoughts and behaviors that disrupt your sleep. We can also explore relaxation techniques like deep breathing and progressive muscle relaxation to calm your body before bed."
           "Good sleep hygiene is essential. This means creating a consistent sleep schedule, avoiding stimulants like caffeine late in the day, and making your bedroom a restful environment. Avoid screens an hour before bed, and try reading or listening to calming music instead. If needed, short-term sleep aids may be used, but therapy and good sleep practices will provide long-term relief."
           """)
else:
   speak("i don't understand..please say hello hey  hi or Doctor Merin. please")
















