---

# Video Splitter Project

This Python script utilizes the `moviepy` library to split a given video into multiple parts based on user-specified duration limits. Each part is then saved as a separate video file.

## Prerequisites

- Python 3.x
- MoviePy library (install via `pip install moviepy`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Video-Splitter.git
    cd Video-Splitter
    ```

2. Run the script:

    ```bash
    python video_splitter.py
    ```

3. Follow the on-screen prompts to provide the file path of the video and set the duration limit for each split.

## Input

The script will prompt you to input the following information:

- **Video File Path:** Enter the file path of the video you want to split.

- **Duration Limit:** Specify the maximum duration (in seconds) for each split video.

## Output

The script will create a new directory in the same location as the input video file. Each split video will be saved in this directory with a filename format like `originalfilename_part1.mp4`, `originalfilename_part2.mp4`, and so on.

Additionally, the script will print information about each split, including the initial and final seconds of each segment.

## Example

Assuming you have a video file named `example_video.mp4`:

```bash
Insert file path of video:
/path/to/example_video.mp4

Enter the limit of seconds that each video must have:
30
```

The script will create a directory named `example_video_parts` and save split videos inside it.

## Notes

- Make sure to install the required libraries before running the script (`pip install moviepy`).

- The script clears the terminal screen for better user interaction.

- If you encounter any issues, ensure that your Python environment meets the prerequisites.

Feel free to contribute or report issues!

---

This README provides users with information on how to use the script, what dependencies
