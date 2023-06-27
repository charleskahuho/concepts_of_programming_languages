import threading
import time

# Define a function that will be run by a thread
def my_function(name):
  print("Thread {} started".format(name))
  # Do some work
  time.sleep(2)
  print("Thread {} finished".format(name))

# Create a thread and start it
thread1 = threading.Thread(target=my_function, args=("Thread 1",))
thread1.start()

# Create another thread and start it
thread2 = threading.Thread(target=my_function, args=("Thread 2",))
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print a message when the threads are finished
print("All threads finished")