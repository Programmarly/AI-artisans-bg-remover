from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta
from backend.cloudinary_manager import CloudinaryManager

class ImageScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.cloudinary_manager = CloudinaryManager()
        self.setup()

    def setup(self):
        """Add jobs to the scheduler."""
        self.scheduler.add_job(
            func=self.cloudinary_manager.remove_old_images,
            trigger="interval",
            minutes=2
        )
        self.scheduler.start()

    def start(self):
        """Start the scheduler."""
        self.scheduler.start()
