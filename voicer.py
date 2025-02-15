from code import TaskList
import pyttsx3

def configure_voice():
    """Configure the text-to-speech engine for optimal voice output"""
    engine = pyttsx3.init()
    
    # Get available voices
    voices = engine.getProperty('voices')
    
    # Set properties for better speech
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    
    # Try to set a clear voice (usually the second voice is better)
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    
    return engine

def format_tasks_for_speech(tasks):
    """Format tasks into a speech-friendly string"""
    if not tasks:
        return "You have no tasks currently."
    
    formatted_tasks = []
    for i, task in enumerate(tasks, 1):
        formatted_tasks.append(f"Task {i}: {task['task']}, Priority {task['priority']}")
    
    return ". ".join(formatted_tasks)

def main():
    task_list = TaskList()
    engine = configure_voice()
    
    try:
        sorted_tasks = task_list.get_sorted_tasks()
        tasks_speech = format_tasks_for_speech(sorted_tasks)
        
        # Greeting with natural pause
        engine.say("Hello ya noor!")
        engine.runAndWait()
        
        # Short pause before listing tasks
        import time
        time.sleep(0.5)
        
        # List the tasks
        engine.say("Here are your tasks in  order:")
        engine.runAndWait()
        
        time.sleep(0.3)  # Brief pause before tasks
        
        engine.say(tasks_speech)
        engine.runAndWait()
        
        # Concluding message
        if sorted_tasks:
            engine.say("Would you like me to help you with any of these tasks?")
        else:
            engine.say("Would you like to add some tasks?")
        engine.runAndWait()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        engine.say("I'm sorry, but I encountered an error while reading your tasks.")
        engine.runAndWait()

if __name__ == "__main__":
    main()