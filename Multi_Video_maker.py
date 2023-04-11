import os
import cv2
import subprocess
import tkinter as tk
from tkinter import filedialog

# Set up the Tkinter file dialog
root = tk.Tk()
root.withdraw()

# Get a list of image file paths using the file dialog
file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

# Set the output video file name and frame rate

print("")
print("                                   Multiple Video Maker ")
print("")
print("")
name = input("  Name of the project" )
print("")
print("                 (Other FPS: -2,-4,-6  , +2,+4,+6,+10)")
print("")
fps = int(input("Enter the desired frame rate for videos: "))
# just in cas if i want to go abck to the old version
#fps_list.append(int(input("Enter the desired frame rate for the video 2: ")))
#print("")
#fps_list.append(int(input("Enter the desired frame rate for the video 3: ")))
#print("")
fps_list = [fps, fps-2, fps-4,fps-6, fps+2, fps+4,fps+6,fps+10]
print("")
print("")

# Set the maximum frame size for the video
#frame_size = (640, 480)
frame_size = (1080, 1920)
#frame_size = (500, 500)


# Loop through each frame rate and create a video
for idx, fps in enumerate(fps_list):
    # Set the output video file name
    output_filename = f"{name}_fps_{fps}.mp4"

    # Set up the video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_path = os.path.join(r"D:\AI Works\Cropped Images Midjourney", "%_Videos_%", output_filename)
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    # Loop through each image file and add it to the video writer
    for file_path in file_paths:
        # Read the image file
        img = cv2.imread(file_path)

        # Calculate the maximum size that fits within the frame size
        max_size = (frame_size[0], int(frame_size[0] * img.shape[0] / img.shape[1]))
        if max_size[1] > frame_size[1]:
            max_size = (int(frame_size[1] * img.shape[1] / img.shape[0]), frame_size[1])

        # Resize the image to the maximum size while preserving the aspect ratio
        img = cv2.resize(img, max_size, interpolation=cv2.INTER_AREA)

        # Add the image to the video writer with black padding if necessary
        pad_top = (frame_size[1] - max_size[1]) // 2
        pad_bottom = frame_size[1] - max_size[1] - pad_top
        pad_left = (frame_size[0] - max_size[0]) // 2
        pad_right = frame_size[0] - max_size[0] - pad_left
        img = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        out.write(img)

    # Release the video writer
    out.release()

    # Rename the video file to include the fps
    new_output_path = os.path.join(r"D:\AI Works\Cropped Images Midjourney", "%_Videos_%", f"{name}_fps_{fps}.mp4")
    os.rename(output_path, new_output_path)

    print(f"Video file saved at: {new_output_path}")

# Open
out_put_videos = r"D:\AI Works\Cropped Images Midjourney\%_Videos_%"
subprocess.Popen(f'explorer "{out_put_videos}"')