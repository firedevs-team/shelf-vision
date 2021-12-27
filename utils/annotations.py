import cv2


def load_annotations(path):
    """
    load annotations from txt file
    """
    with open(path, "r") as f:
        lines = f.readlines()
    annotations = []
    for line in lines:
        annotation = line.strip().split(" ")
        annotations.append(annotation)
    return annotations


def draw_bbox(img, bbox, color=(0, 255, 0)):
    """
    draw bbox on image
    """
    x1, y1, x2, y2 = bbox
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    return img


def draw_bboxes(img, bboxes, color=(0, 255, 0)):
    """
    draw bboxes on image
    """
    for bbox in bboxes:
        img = draw_bbox(img, bbox, color)
    return img
