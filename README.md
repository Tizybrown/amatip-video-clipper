# Amatip Digital Box - Video Clipper Tool

Welcome to **Amatip Digital Box - Video Clipper Tool**! This project is designed to help users clip sections from their videos effortlessly using AI.

## Features

- **Video Upload**: Upload videos directly from your local machine or paste video URLs.
- **AI Video Clipping**: Automatically clip the best moments of your video using AI.
- **Video Preview**: Preview the selected section of the video before final clipping.
- **Save and Download**: After clipping the video, save it and download it directly.
  
## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Bootstrap for responsive design)
- **Backend**: Python (Flask/FastAPI/Django for server-side logic)
- **AI**: AI-based algorithms for automatic video clipping (to be integrated)
- **Video Processing**: FFmpeg or similar tools for video processing and editing.

## Installation

To run this project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Tizybrown/amatip-video-clipper.git
    ```

2. Navigate to the project directory:
    ```bash
    cd amatip-video-clipper
    ```

3. Install dependencies (if applicable):
    For Python-based backend (Flask/Django/FastAPI):
    ```bash
    pip install -r requirements.txt
    ```

    For frontend, you may need to install additional dependencies such as `npm` or `yarn` for React or Vue:
    ```bash
    npm install
    ```

4. Start the server:
    For a Python backend (Flask):
    ```bash
    python app.py
    ```

    For other backends (Django/FastAPI), run the respective commands to start the server.

## How It Works

1. **Video URL Upload**: You can paste the URL of a video from platforms like YouTube, Vimeo, or upload a local video from your computer.
2. **Video Clipping**: The tool will automatically detect the best moments in the video using AI algorithms. You can also manually select the start and end times for clipping.
3. **Download**: After processing, you can download the clipped section of the video.

## Screenshots



## Usage Example

1. Go to the **Amatip Digital Box - Clip Your Videos With AI** page.
2. Paste your video URL or upload your video file.
3. Choose the clip section.
4. Hit the **Clip Video** button and watch AI automatically select the best moments.
5. Save and download the clipped video.

## Contributing

We welcome contributions! If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your changes and create a pull request.

## License


## Contact



*Thank you for using Amatip Digital Box!*






# Amatip Video Clipper - API Endpoints Documentation

This document provides the necessary API endpoints for the **Amatip Digital Box** video clipping tool. These endpoints are used for uploading videos, generating clips, and downloading the clipped content.

## API Endpoints

### 1. Upload Video
- **Endpoint**: `/api/upload_video`
- **Method**: `POST`
- **Description**: Upload a video either by providing a video file or a URL.
  
#### Request Body:
- If uploading a video file:
  ```json
  {
    "file": "<video_file>"
  }
  ```
- If uploading via URL:
  ```json
  {
    "url": "<video_url>"
  }
  ```

#### Response:
```json
{
  "status": "success",
  "message": "Video uploaded successfully",
  "video_id": "<generated_video_id>"
}
```

### 2. Get Video Preview
- **Endpoint**: `/api/video_preview/<video_id>`
- **Method**: `GET`
- **Description**: Retrieve the preview of the uploaded video for review before clipping.

#### Request:
- URL parameter: `video_id` (The ID of the uploaded video)

#### Response:
```json
{
  "status": "success",
  "video_url": "<preview_video_url>"
}
```

### 3. Clip Video
- **Endpoint**: `/api/clip_video`
- **Method**: `POST`
- **Description**: Clip a specific section of the uploaded video by providing the start and end times.

#### Request Body:
```json
{
  "video_id": "<generated_video_id>",
  "start_time": "00:01:00",  // Start time in HH:MM:SS
  "end_time": "00:03:00"     // End time in HH:MM:SS
}
```

#### Response:
```json
{
  "status": "success",
  "message": "Video clipped successfully",
  "clipped_video_url": "<clipped_video_url>"
}
```

### 4. Download Clipped Video
- **Endpoint**: `/api/download_clipped_video/<video_id>`
- **Method**: `GET`
- **Description**: Download the clipped video once it is processed.

#### Request:
- URL parameter: `video_id` (The ID of the clipped video)

#### Response:
- The server will respond with a direct download link or file depending on the backend's file handling approach.

### 5. Cancel Video Clipping
- **Endpoint**: `/api/cancel_clipping`
- **Method**: `POST`
- **Description**: Allows the user to cancel the video clipping process if it's in progress.

#### Request Body:
```json
{
  "video_id": "<generated_video_id>"
}
```

#### Response:
```json
{
  "status": "success",
  "message": "Clipping process canceled"
}
```

## Usage Notes
- The video ID is a unique identifier generated when a video is uploaded.
- The `start_time` and `end_time` for clipping should be in the format `HH:MM:SS`.
- After clipping a video, the `clipped_video_url` will provide a link to download or view the clipped content.
- You can cancel a clipping process by sending the video ID to the `cancel_clipping` endpoint.

---

## Example Usage

1. **Upload Video**  
   Upload a video from your local machine or via URL using the `/api/upload_video` endpoint.

2. **Get Preview**  
   Retrieve a preview of the uploaded video by calling `/api/video_preview/{video_id}`.

3. **Clip Video**  
   Select a start and end time, and use the `/api/clip_video` endpoint to generate the clip.

4. **Download Clipped Video**  
   Once the clipping is complete, the video will be available for download using the `/api/download_clipped_video/{video_id}` endpoint.

---

## How to Use with Frontend

1. **Call Upload Video Endpoint**: The frontend will call the `/api/upload_video` endpoint with the appropriate data (file or URL).
2. **Call Get Video Preview**: After the video is uploaded, the frontend can use the `/api/video_preview/{video_id}` endpoint to fetch and display a preview of the video.
3. **Call Clip Video Endpoint**: When the user selects the clip start and end times, the frontend will send these details to the `/api/clip_video` endpoint to process the clipping.
4. **Call Download Clipped Video Endpoint**: Once the video is clipped, the frontend can provide the user with a link to download the clipped video using `/api/download_clipped_video/{video_id}`.
5. **Optional - Cancel Clipping**: The frontend can send a cancellation request to the `/api/cancel_clipping` endpoint if needed.

---

### Notes:
- The endpoints provided are part of the Amatip Video Clipper tool.
- Ensure proper error handling is in place for each API call, such as handling invalid video IDs or missing parameters.

---
