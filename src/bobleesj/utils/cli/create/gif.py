import os
import moviepy
from moviepy.video.fx import MultiplySpeed

def create(args):
    if not getattr(args, "path", None):
        print("No path provided.")
        return

    video_path = args.path
    if not os.path.isfile(video_path):
        print(f"File not found: {video_path}")
        return

    speed = getattr(args, "speed", 1.0)
    try:
        speed = float(speed)
        if speed <= 0:
            raise ValueError()
    except Exception:
        print("Invalid speed; must be > 0.")
        return

    framerate = getattr(args, "framerate", 10)
    try:
        framerate = int(framerate)
        if framerate <= 0:
            raise ValueError()
    except Exception:
        print("Invalid framerate; must be a positive integer.")
        return

    base, _ = os.path.splitext(video_path)
    gif_path = base + ".gif"
    try:
        print(f"Converting to GIF: {gif_path} (speed: {speed}x, fps: {framerate})")
        with moviepy.VideoFileClip(video_path) as clip:
            if speed != 1.0:
                clip = clip.with_effects([MultiplySpeed(speed)])
            clip.write_gif(gif_path, fps=framerate)
        print("GIF created!")
    except Exception as e:
        print(f"Failed to create GIF: {e}")
