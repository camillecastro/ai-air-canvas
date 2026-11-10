"""AI Air Canvas — draw in the air using hand tracking."""
import cv2
import mediapipe as mp
import numpy as np
from pathlib import Path
from datetime import datetime

COLORS = [
    (255, 100, 30),   # Blue
    (50, 200, 70),    # Green
    (40, 80, 240),    # Red
    (230, 70, 210),   # Pink
    (255, 255, 255),  # White
]
NAMES = ["Blue", "Green", "Red", "Pink", "White"]

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    hands = mp.solutions.hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.65,
        min_tracking_confidence=0.55,
    )

    canvas = None
    previous = None
    color_idx = 0
    eraser = False
    show_camera = True

    Path("screenshots").mkdir(exist_ok=True)

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            height, width = frame.shape[:2]

            if canvas is None or canvas.shape != frame.shape:
                canvas = np.zeros_like(frame)
                previous = None

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                landmarks = result.multi_hand_landmarks[0].landmark

                index_up = landmarks[8].y < landmarks[6].y
                middle_up = landmarks[12].y < landmarks[10].y

                x = int(landmarks[8].x * width)
                y = int(landmarks[8].y * height)

                point = (
                    max(0, min(width - 1, x)),
                    max(0, min(height - 1, y)),
                )

                if index_up and not middle_up:
                    if previous is not None:
                        if eraser:
                            cv2.line(canvas, previous, point, (0, 0, 0), 34)
                        else:
                            cv2.line(
                                canvas, previous, point,
                                COLORS[color_idx], 7, cv2.LINE_AA
                            )
                    previous = point
                else:
                    previous = None

                cv2.circle(frame, point, 9, (0, 255, 255), -1)
            else:
                previous = None

            if show_camera:
                display = frame.copy()
                mask = np.any(canvas > 0, axis=2)
                blended = cv2.addWeighted(frame, 0.25, canvas, 0.75, 0)
                display[mask] = blended[mask]
            else:
                display = canvas.copy()

            cv2.rectangle(display, (0, 0), (width, 75), (25, 25, 25), -1)

            selected = "Eraser" if eraser else NAMES[color_idx]
            cv2.putText(
                display, f"AI AIR CANVAS | {selected}",
                (12, 28), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2
            )
            cv2.putText(
                display, "1-5 Colors | E Erase | C Clear | B Background | S Save | Q Quit",
                (12, 55), cv2.FONT_HERSHEY_SIMPLEX,
                0.43, (255, 255, 255), 1
            )

            cv2.imshow("AI Air Canvas", display)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q") or key == 27:
                break
            elif ord("1") <= key <= ord("5"):
                color_idx = key - ord("1")
                eraser = False
            elif key == ord("e"):
                eraser = not eraser
            elif key == ord("c"):
                canvas[:] = 0
                previous = None
            elif key == ord("b"):
                show_camera = not show_camera
            elif key == ord("s"):
                filename = datetime.now().strftime("air-canvas-%Y%m%d-%H%M%S.png")
                path = Path("screenshots") / filename
                cv2.imwrite(str(path), display)
                print(f"Saved: {path}")

    finally:
        cap.release()
        hands.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



    