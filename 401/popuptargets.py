import os

def create_dummy_files():
    directory = '/home/opslab/Documents/git/opschallenges/dummies/'
    sentences = "This is sentence one. This is sentence two."

    # Make sure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Loop to create files
    for i in range(1, 6):  # This will create files from filename1.txt to filename5.txt
        file_path = os.path.join(directory, f'filename{i}.txt')
        with open(file_path, 'w') as file:
            file.write(sentences)

create_dummy_files()
