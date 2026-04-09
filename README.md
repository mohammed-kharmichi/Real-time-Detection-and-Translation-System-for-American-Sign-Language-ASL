# Real-time Detection and Translation System for American Sign Language (ASL)

## Technologies
- **Python** - OpenCV2, Pandas, MediaPipe, OS, Sklearn, Toglib

## Context
This project originated from the need to create a technological solution that facilitates communication for individuals using ASL, as well as for those looking to learn this language. The goal is to bridge the gap between deaf or non-verbal individuals and the rest of society by providing an accessible and effective tool for visual communication. Through this project, we aim to promote inclusion and accessibility for all, recognizing the diversity of communication modes.

## American Sign Language "ASL"
ASL is much more than just a set of gestures. It is a complete language with its own grammar, syntax, and distinct vocabulary. Primarily used in the United States and Canada, ASL offers a means of expression for individuals whose vocal communication is limited or absent. Its richness and complexity make it a powerful mode of communication adaptable to a wide variety of contexts.

## Objectives
The main objectives of the ASL detection system are as follows:

- Development of a robust system capable of detecting ASL in real time
- Use of MediaPipe for extracting relevant hand points
- Design of a training and testing database
- Creation of the Machine Learning model
- Testing the model
- Providing an intuitive user interface to interact with the system

---

## Dataset Architecture

### Overview
The dataset was created manually and is organized in a structured folder hierarchy. Each subfolder represents a specific ASL class (sign interpretation), containing multiple images of that particular sign.

### Dataset Structure

```
DataSet/
├── 1/
│   ├── image_1.jpg
│   ├── image_2.jpg
│   └── ...
├── 2/
│   ├── image_1.jpg
│   ├── image_2.jpg
│   └── ...
├── a/
│   ├── image_1.jpg
│   ├── image_2.jpg
│   └── ...
├── salut/
│   ├── image_1.jpg
│   ├── image_2.jpg
│   └── ...
└── ...
```

### Dataset Characteristics
- **Structure**: Each subfolder name corresponds to a unique ASL class (sign interpretation)
- **Content**: Multiple training images per class capturing different hand positions and angles
- **Classes Examples**: Numbers (1, 2, ...), Letters (a, b, ...), Words (salut, merci, ...)
- **Purpose**: These images serve as the training data for the Machine Learning model to learn and recognize different ASL signs

### Example Classes

#### Class "2" - Number Two
The class "2" contains multiple images showing the ASL gesture for the number two from different perspectives and hand positions.

| Image 1 | Image 2 |
|---------|---------|
| ![Class 2 - Image 1](Readme_Images/2/image1.jpg) | ![Class 2 - Image 2](Readme_Images/2/image2.jpg) |

#### Class "merci" - Thank You
The class "merci" contains images demonstrating the ASL sign for "thank you" with various hand positions and angles.

| Image 1 | Image 2 |
|---------|---------|
| ![Class merci - Image 1](Readme_Images/merci/image1.jpg) | ![Class merci - Image 2](Readme_Images/merci/image2.jpg) |

---

## Landmark Extraction Process

### Overview
The landmark extraction process is the foundation of our ASL detection system. It uses **MediaPipe** and **OpenCV** to identify and extract the precise coordinates of hand keypoints from images, which are then used to train the Machine Learning model.

### Hand Landmarks Visualization

The following diagram shows the 21 hand landmarks detected by MediaPipe for each hand:

![Hand Landmarks](Readme_Images/handlandmarks.jpg)

These 21 keypoints represent crucial points on the hand, including:
- **Wrist** (1 point)
- **Palm** (5 points - base of each finger)
- **Fingers** (15 points - 3 points per finger: tip, middle, and base)

Each landmark contains:
- **X coordinate**: Horizontal position (0 to image width)
- **Y coordinate**: Vertical position (0 to image height)
- **Z coordinate**: Depth information (relative hand depth)

### How It Works

#### 1. **Image Processing with OpenCV**
The process begins with image preprocessing using OpenCV:
- Images are read in BGR color format
- Converted to RGB format (required by MediaPipe)
- Image dimensions are extracted for coordinate scaling

#### 2. **Hand Landmark Extraction**
MediaPipe detects hands in the processed image and extracts 21 keypoints for each detected hand:
- The landmarks capture the complete hand structure
- Coordinates are normalized relative to image dimensions
- Both hands can be detected simultaneously (up to 2 hands per image)

#### 3. **Data Organization**
For each image, the system captures:
- **Class label**: The ASL sign class (e.g., "merci", "2", "salut")
- **First hand landmarks**: 21 points × 3 coordinates = 63 values
- **Hand count**: Indicator (0 = one hand, 1 = two hands)
- **Second hand landmarks**: 21 points × 3 coordinates = 63 values (if two hands detected)

### Output Format: hands_data.txt

The extraction process generates a `hands_data.txt` file containing:

```
class    ld_1_1    ld_1_2    ...    ld_1_63    o_h    ld_2_1    ld_2_2    ...    ld_2_63
merci    142.5     89.3      ...    23.1       0      0         0        ...    0
2        156.2     94.7      ...    31.2       1      201.3     88.5     ...    18.9
salut    149.1     91.2      ...    26.4       0      0         0        ...    0
...
```

**Format Details:**
- **class**: ASL sign class name
- **ld_1_1 to ld_1_63**: 63 landmark coordinates for first hand (21 landmarks × 3 coordinates)
- **o_h**: Hand occurrence indicator (0 = one hand, 1 = two hands)
- **ld_2_1 to ld_2_63**: 63 landmark coordinates for second hand (zeros if only one hand detected)

### Key Technologies

#### MediaPipe
- **Purpose**: Detects hands in images and extracts 21 hand keypoints with high accuracy
- **Advantages**: 
  - Real-time performance
  - Works with various lighting conditions
  - Robust hand detection
  - Provides 3D coordinates (x, y, z)

#### OpenCV (cv2)
- **Purpose**: Handles image I/O operations and color space conversions
- **Functions used**:
  - `cv2.imread()`: Load images from dataset
  - `cv2.cvtColor()`: Convert BGR to RGB format
  - Image dimension extraction for coordinate normalization

#### Feature Engineering
- **Coordinate Scaling**: Landmarks are scaled relative to image dimensions for scale invariance
- **Multi-hand Support**: System handles 1-2 hands per image
- **3D Information**: Z-coordinates provide depth information for hand position

### Dataset Generation Workflow

```
DataSet Folder (Images)
        ↓
   OpenCV Reading
        ↓
   Image Conversion (BGR → RGB)
        ↓
   MediaPipe Detection
        ↓
   Extract 21 Landmarks per Hand
        ↓
   Normalize Coordinates
        ↓
   Format Data
        ↓
   hands_data.txt (Training Data)
        ↓
   Machine Learning Model Training
```

### Why This Matters

The landmark extraction process:
1. **Transforms images** into numerical features that ML models can understand
2. **Reduces dimensionality** from thousands of pixels to 127 meaningful features
3. **Captures hand structure** in a way that is scale and translation invariant
4. **Creates a unified representation** of different hand poses and signs
5. **Enables real-time processing** by focusing on relevant hand data only

This feature-rich dataset becomes the foundation for training an accurate and efficient ASL recognition model.

---

*This project demonstrates the power of combining computer vision (MediaPipe + OpenCV) with machine learning to solve real-world accessibility challenges.*