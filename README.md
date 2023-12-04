# Yolov5s+

## Installation

```
git clone https://github.com/kevin0929/Yolov5s-plus.git
cd Yolov5s-plus
pip install -r requirements.txt  # install dependencies
```

## Tracking

```bash
$ python track.py
```

<details>
<summary>Tracking methods</summary>

```bash
$ python track.py --tracking-method strongsort
                                    ocsort
                                    bytetrack
```
  
</details>

<details>
<summary>Tracking sources</summary>

Tracking can be run on most video formats

```bash
$ python track.py --source 0  # webcam
                           img.jpg  # image
                           vid.mp4  # video
                           path/  # directory
                           path/*.jpg  # glob
                           'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

</details>
  
<details>
<summary>Filter tracked classes</summary>

By default the tracker tracks all MS COCO classes.

If you want to track a subset of the classes that you model predicts, add their corresponding index after the classes flag,

```bash
python track.py --source 0 --yolo-weights yolov5s.pt --classes 16 17  # COCO yolov5 model. Track cats and dogs, only
```
