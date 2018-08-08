source venv/Scripts/activate
flow --model src/model/cfg/tiny-yolo-voc.cfg --load bin/tiny-yolo-voc.weights --train --annotation ../resources/annotations --dataset ../resources/imgData