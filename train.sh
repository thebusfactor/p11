source venv/Scripts/activate
flow --model cfg/tiny-yolo-voc-1c.cfg --load bin/tiny-yolo-voc.weights --train --annotation ../resources/annotations --dataset ../resources/imgData --gpu 0.8
