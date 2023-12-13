# ReadMe
### Purpose of this repository
This repository is for the submission of the final project for the CS 437 EKS class. The code in this repository was either provided by the class or developed by Avery Plote and Nikunj Tyagi. The project is on using a corner reflector's movement to do radar backscatter communication, what we call "CornerComm."
### Contents of this repository
- `Example files.zip` : Contains example radar binary data folders to see how the data processing worked in different situations
- `Final.cfg` : The config file used to run the radar
- `Servo holder.zip` : This contains the CAD files we made to make something to hold the servo
- `Visualizer.zip` : Contains the files (and instructions) needed to run the radar and collect the data
- `final_project.ipynb` : The Jupyter notebook that contains the data processing code
- `parseTLVs.py` and `parse_bin_output.py` : Files that contain helper functions used as part of the data processing. The files were provided by the class.
- `run_servo.py` : This file contains the code needed to run 
### Hardware Setup
Connect the radar to a computer using the USB cable. Take note of what port is being used. Follow instructions in `Visualizer.zip`.
To setup the corner reflector, you will need a 3-wire 5V servo. The Tower Pro 9g is what we used. Wire up the servo to pins 4 (5V power), 6 (ground), and 11 (GPIO17). Other pins could be used but would require modification of the code in `run_servo.py`.
To setup the corner reflector, attach it to the servo securely. We used a small binder clip. It may also be helpful to have an enclosure or some structure to securely hold the servo. If you have the ability, you can print the servo holder in `Servo holder.zip` to do this job.
### How to run the code / use the system
##### Radar
Using the COM port you took note of, use the visualizer GUI to run the radar. Use Final.cfg as the config file. The data will automatically be saved to a folder of bin files. 
##### Raspberry Pi
If the servo has been wired up correctly, running run_servo.py should result in the reflector turning. To change the binary string being sent, modify the `string` variable in the file.
##### Data Processing
Access the `final_project.ipynb` jupyter notebook. In the notebook, you will need to replace binFilePath with the path to the folder that your binary files are contained in for the specific run you want to analyze. Additionally, modify the num_files variable to indicate the number of binary files in your folder. Lastly, you may find on occasion that you need to modify the height parameter in the find_peaks function to result in better data processing. 
### Radar Data
There are a few example files that are included in `Example files.zip` that can be used to run the data processing part of the project and see how the system worked in different situations. More data can be found in the `Visualizer.zip` folder but that includes all of our data collected for many different runs and even for different projects.
### Special Instructions
If you have not set up the radar or the GUI to collect the radar data, follow the instructions in `Visualizer.zip`.
