import os
import shutil

class cCleanUp():
    def __init__(self) -> None:
        pass

    def delete_pycache(self, directory : list) -> None:
        for directory in directory:
            for root, dirs, files in os.walk(directory):
                if '__pycache__' in dirs:
                    pycache_dir = os.path.join(root, '__pycache__')
                    shutil.rmtree(pycache_dir)


if __name__ == "__main__":
    oCleanUp = cCleanUp()
    target_directory = ["./VoiceGptLib/Auxiliary",
                        "./VoiceGptLib/ChatGPT",
                        "./VoiceGptLib/Runtime",
                        "./VoiceGptLib/Voice"
                        ]
    oCleanUp.delete_pycache(target_directory)