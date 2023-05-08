"""Example program to show how to read a multi-channel time series from LSL."""
import csv

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

eeg_data = []
header = ["timestamp", "channel1", "channel2", "channel3", "channel4", "channel5", "channel6", "channel7", "channel8"]

try:
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        eeg_data.append([timestamp, *sample])
        print(timestamp, sample)
except KeyboardInterrupt:
    with open('eeg_data16.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        
        # write the data
        writer.writerow(header)
        writer.writerows(eeg_data)
    print('Data collected and exported!')
    


