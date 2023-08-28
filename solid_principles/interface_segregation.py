"""
The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use.
In other words, it suggests that you should design interfaces that are specific to the needs of the clients using them, rather than creating large, monolithic interfaces that encompass more than what a client requires.
"""


# Here are a few examples to help explain the Interface Segregation Principle:

#  Example 1: Violation of ISP

class Worker:
    def work(self):
        pass

    def eat(self):
        pass


# In this example,
# the Worker interface includes both the work and eat methods.
# If a client only needs the ability to perform work, it would still be forced to implement the eat method, violating ISP.

# Example 2: Applying ISP

class Workable:
    def work(self):
        pass


class Eatable:
    def eat(self):
        pass


class Worker(Workable, Eatable):
    pass


"""
In this improved version, 
the Workable and Eatable interfaces are segregated, 
and the Worker class can implement both interfaces separately. 
Clients can now choose to implement only the interfaces they need.
"""


# Example 3: Multimedia Player

class AudioPlayer:
    def play_audio(self):
        pass


class VideoPlayer:
    def play_video(self):
        pass


class MediaPlayer(AudioPlayer, VideoPlayer):
    pass


"""
In this scenario, a MediaPlayer class attempts to combine both audio and video capabilities. 
If a client only wants to work with audio, they’re still forced to have the video-related methods. 
Splitting the interfaces as per ISP would provide more flexibility.
"""

"""
By adhering to the Interface Segregation Principle, 
you ensure that your interfaces are tailored to the specific requirements of clients, 
leading to more maintainable and adaptable code.
"""
