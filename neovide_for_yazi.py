import subprocess
import os
import sys
import time
import threading


class Instance:
    def __init__(self) -> None:
        self.current_directory = os.getcwd()
        self.term_pid = subprocess.check_output(
            "ps aux | grep kitty | grep -v grep | tail -n 1 | awk '{print $2}'",
            shell=True,
            text=True,
        ).strip()
        command = (
            ["setsid", "neovide"]
            if len(sys.argv) < 2
            else ["setsid", "neovide", sys.argv[1]]
        )
        self.neovide_process = subprocess.Popen(command)
        self.isActive = True
        self.thread = threading.Thread(target=self.monitor)
        self.thread.daemon = True
        self.thread.start()

        while self.isActive:
            time.sleep(1)

    def monitor(self):
        subprocess.Popen(["kill", self.term_pid])
        while self.isActive:
            time.sleep(1)
            if self.neovide_process.poll() is not None:
                self.open_new_terminal()
                break

    def open_new_terminal(self):
        try:
            subprocess.run(["setsid", "kitty", "--directory", self.current_directory])
        except Exception:
            pass
        self.isActive = False


if __name__ == "__main__":
    instance = Instance()
