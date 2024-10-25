import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")
            file_name=event.src_path.split('/')
            self.move_file(file_name[-1])

    def move_file(self,file_name):
        print(f'move file called with file {file_name}')
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Define the full path for the 'files' folder on the desktop
        files_folder_path = os.path.join(desktop_path, 'files')
    
    # Check if the 'files' folder exists
        if os.path.exists(files_folder_path) and os.path.isdir(files_folder_path):
            print("The 'files' folder already exists on the desktop.")
            shutil.move('/Users/rakspant/Desktop/'+file_name, '/Users/rakspant/Desktop/files')
        else:
            print("The 'files' folder does not exist on the desktop.")
            try:
        # Create the folder
                
                os.makedirs('/Users/rakspant/Desktop/files', exist_ok=True)
                print(f"Folder created successfully at: /Users/rakspant/Desktop")
                shutil.move('/Users/rakspant/Desktop/'+file_name, '/Users/rakspant/Desktop/files')
                
            except OSError as e:
                print(f"Error creating folder: {e}")


    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    path = "/Users/rakspant/Desktop"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()