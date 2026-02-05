from ultralytics import YOLO
import cv2

class YoloVision():
    def __init__(self):
        self.model_obj = YOLO('yolov8s-world.pt')
        self.model_pose = YOLO('yolo26n-pose.pt')
        self.model_obj.set_classes(['person', 'food', 'drink', 'bottle', 'cup'])
        self.latest_vision = (None, None)
        self.frame_count = 0
        self.last_plotted_frame = None

    def see(self, frame):
        last_detected_objs, last_detected_poses = None, None
        results_objs = None

        if self.frame_count % 2 == 0:
            results_objs = self.model_obj(frame, verbose=False, imgsz=416)
            last_detected_objs = results_objs[0]
        else:
            results_pose = self.model_pose(frame, verbose=False, conf=0.5, imgsz=416)
            last_detected_poses = results_pose[0]

        self.latest_vision = last_detected_objs if self.frame_count % 2 == 0 else self.latest_vision[0], last_detected_poses if self.frame_count % 2 != 0 else self.latest_vision[1]
        self.frame_count += 1

        self.last_plotted_frame = results_objs[0].plot() if results_objs else self.last_plotted_frame if self.last_plotted_frame.any() else frame
        cv2.imshow("Frame", self.last_plotted_frame)

        return self.latest_vision
