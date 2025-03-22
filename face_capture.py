# import cv2
# import os
# import psycopg2

# def get_user_email(user_id):
#     """Fetch user email from the database using user_id."""
#     conn = psycopg2.connect(database="your_db", user="your_user", password="your_password", host="your_host", port="your_port")
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT mailid FROM users WHERE id = %s", (user_id,))
#     result = cursor.fetchone()
    
#     conn.close()
#     return result[0] if result else None

# def capture_frames(user_id, base_folder="captured_faces", num_frames=52):
#     """Capture frames and save them using the registered user's email."""
    
#     email = get_user_email(user_id)
#     if not email:
#         print("❌ Error: User not found!")
#         return
    
#     # Convert email to a folder-friendly format
#     email_folder = email.replace("@", "_").replace(".", "_")
#     output_folder = os.path.join(base_folder, email_folder)

#     # Create directory if it doesn’t exist
#     os.makedirs(output_folder, exist_ok=True)

#     # Open webcam
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("❌ Error: Could not access webcam!")
#         return

#     print(f"📷 Capturing frames for {email}...")

#     frame_count = 0
#     while frame_count < num_frames:
#         ret, frame = cap.read()
#         if not ret:
#             print("❌ Error: Could not read frame!")
#             break

#         frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)
#         frame_count += 1

#         try:
#             cv2.imshow("Capturing Frames", frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         except cv2.error:
#             pass

#     cap.release()
#     cv2.destroyAllWindows()
#     print(f"✅ Captured {frame_count} frames in '{output_folder}'.")

# # Call this function after a successful registration
# if __name__ == "__main__":
#     user_id = input("Enter your user ID: ").strip()  # This should be passed automatically
#     capture_frames(user_id)


# import cv2
# import os

# def capture_frames(output_folder="captured_faces", num_frames=52):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Open webcam
#     cap = cv2.VideoCapture(0)
    
#     if not cap.isOpened():
#         print("Error: Could not access the webcam.")
#         return
    
#     print("Capturing frames... Press 'q' to exit early (if display is available).")
    
#     frame_count = 0
#     while frame_count < num_frames:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Could not read frame.")
#             break
        
#         # Save frame as an image file
#         frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)
        
#         frame_count += 1
        
#         # Try displaying the frame; if not supported, skip displaying
#         try:
#             cv2.imshow("Capturing Frames", frame)
#             # Press 'q' to exit early (only works if display is supported)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         except cv2.error:
#             # GUI functions are not available (likely running in a headless environment)
#             pass
    
#     # Release resources
#     cap.release()
#     # Destroy any OpenCV windows (if they were created)
#     try:
#         cv2.destroyAllWindows()
#     except cv2.error:
#         pass
        
#     print(f"Captured {frame_count} frames in '{output_folder}'.")

# if __name__ == "__main__":
#     capture_frames()


import cv2
import os

def format_email_folder(email):
    """Convert email into a valid folder name."""
    return email.replace("@", "_").replace(".", "_")

def capture_frames(email, base_folder="captured_faces", num_frames=52):
    """Capture frames and save them in a folder named after the email ID."""
    
    # Format email for folder name
    email_folder = format_email_folder(email)
    output_folder = os.path.join(base_folder, email_folder)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return
    
    print(f"Capturing frames for {email}... Press 'q' to exit early.")

    frame_count = 0
    while frame_count < num_frames:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Save frame inside the user's folder
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
        
        # Display frame (optional)
        # cv2.imshow("Capturing Frames", frame)
        try:
            cv2.imshow("Capturing Frames", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except cv2.error:
            pass  # Ignore GUI errors

    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
        
    print(f"Captured {frame_count} frames in '{output_folder}'.")

if __name__ == "__main__":
    user_email = input("Enter your email: ").strip()  # Get user email
    capture_frames(user_email)

# import cv2
# import os
# import numpy as np
# import face_recognition
# import sqlite3

# # Function to format email for folder name
# def format_email_folder(email):
#     return email.replace("@", "_").replace(".", "_")

# # Function to store face encoding in the database
# def store_encoding(email, encoding):
#     conn = sqlite3.connect("face_data.db")
#     cursor = conn.cursor()

#     # Create table if not exists
#     cursor.execute('''CREATE TABLE IF NOT EXISTS faces 
#                       (email TEXT PRIMARY KEY, encoding BLOB)''')

#     # Convert encoding array to bytes
#     encoding_bytes = encoding.tobytes()

#     # Store in DB
#     cursor.execute("INSERT OR REPLACE INTO faces (email, encoding) VALUES (?, ?)", (email, encoding_bytes))
#     conn.commit()
#     conn.close()

# # Function to capture frames and store encoding
# def capture_frames(email, base_folder="captured_faces", num_frames=10):
#     email_folder = format_email_folder(email)
#     output_folder = os.path.join(base_folder, email_folder)

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not access the webcam.")
#         return

#     print(f"📸 Capturing frames for {email}...")

#     face_encodings = []
#     frame_count = 0

#     while frame_count < num_frames:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         # Save frame
#         frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)

#         # Convert frame to RGB and get face encoding
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         encodings = face_recognition.face_encodings(rgb_frame)

#         if encodings:
#             face_encodings.append(encodings[0])  # Store first detected face encoding

#         frame_count += 1

#     cap.release()
#     cv2.destroyAllWindows()

#     # Store the first detected face encoding in the database
#     if face_encodings:
#         avg_encoding = np.mean(face_encodings, axis=0)  # Average face encoding
#         store_encoding(email, avg_encoding)
#         print(f"✅ Face encoding stored in database for {email}")
#     else:
#         print("⚠️ No face detected. Try again.")

