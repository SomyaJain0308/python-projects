"""
Terminal Styling with Curses: Uses the curses library to create a dynamic, responsive interface in the terminal, allowing for 
                              real-time screen updates without flickering.
Real-time Feedback: As the user types, the application overlays their input onto the target text, instantly highlighting correct 
                    characters in green and incorrect characters in red.
Performance Calculation: The project calculates and displays the user's WPM in real-time by tracking the elapsed time using the 
                         time.time() function, comparing the start time to the current system time.
Interactive Loop: Includes a start screen that waits for any key press to begin, and a post-test screen that prompts the user 
                  to either restart the test or exit using the Escape key.
Text Handling: Manages user input by clearing the screen and refreshing the display on every keystroke, ensuring that only the 
               current state of the typing test is visible.
"""
# I am not doing this wth is the point of doing this project no fucking way I am using this curses library every again and if that's the case then wtf would i go through the trouble of doing the projects and learning all those lame ass defines functions bruh