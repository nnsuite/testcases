### Mobilenet_v1_1.0_224_quant
* Model data
  - 224x224 image classification, Quantized models, Model size (4.3 Mb)
  - Download the quantized modelfrom [Here](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/g3doc/models.md#image-classification-quantized-models)
  - Paper - https://arxiv.org/pdf/1712.05877.pdf
* Label data
  - Download the label data from [Here](https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/contrib/lite/java/demo/app/src/main/assets/labels_mobilenet_quant_v1_224.txt)


### ssd_mobilenet_v2_coco
* Model data
  - 300x300 image object SSD(Single Shot Multibox Detection) model
  - more information at [Here](https://github.com/tensorflow/models/tree/master/research/object_detection)

### conv_actions_tflite
* Model data
  - Speech command pretrained model ([Audio format](https://developer.android.com/reference/android/media/AudioFormat#ENCODING_PCM_16BIT) 16-bit signed integer, 16k mono pcm)
  - Downloded from [Here](https://storage.googleapis.com/download.tensorflow.org/models/tflite/conv_actions_tflite.zip)

### add_tflite
* Model data
  - Downloaded from [Here](https://review.tizen.org/gerrit/gitweb?p=platform/core/ml/nnfw.git;a=blob;f=nnpackage/examples/one_op_in_tflite/add.tflite;h=e748b6843646a295dfe5e701cf22259bb93adc6e;hb=refs/heads/accepted/tizen_5.5_unified)
  - Performs basic addition - adds `2.0` to the input data
  - Supports flexible shape for input data
