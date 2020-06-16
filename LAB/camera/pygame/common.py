# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Common utilities."""
import numpy as np
import tflite_runtime.interpreter as tflite

EDGETPU_SHARED_LIB = 'libedgetpu.so.1'

def make_interpreter(model_file):
    model_file, *device = model_file.split('@')
    return tflite.Interpreter(
      model_path=model_file,
      experimental_delegates=[
          tflite.load_delegate(EDGETPU_SHARED_LIB,
                               {'device': device[0]} if device else {})
      ])

def input_image_size(interpreter):
    """Returns input image size as (width, height, channels) tuple."""
    _, height, width, channels = interpreter.get_input_details()[0]['shape']
    return width, height, channels

def input_tensor(interpreter):
    """Returns input tensor view as numpy array of shape (height, width, 3)."""
    tensor_index = interpreter.get_input_details()[0]['index']
    return interpreter.tensor(tensor_index)()[0]

def output_tensor(interpreter, i, dense_layer_weight, scaling = False):
    """Returns dequantized output tensor if quantized before."""
    output_details = interpreter.get_output_details()[i]
    output_activation = np.squeeze(interpreter.tensor(output_details['index'])())
    print('final convoltuion tensor :', output_activation.shape)

    if 'quantization' not in output_details:
        return output_activation
    scale, zero_point = output_details['quantization']

    CAM = np.zeros(dtype=np.float32, shape=output_activation.shape[0:2])
    if scaling == True :
        if scale == 0:
            for index, weight in enumerate(dense_layer_weight[:,0]):
                CAM += weight * output_activation[:, :, index]
            return CAM
        else :
            for index, weight in enumerate(dense_layer_weight[:,0]):
                CAM += (weight * scale * (output_activation[:, :, index] - zero_point))
            return CAM
    else :
        for index, weight in enumerate(dense_layer_weight[:, 0]):  # 0 instead of image_class. because 1 is Noobj
            CAM += weight * output_activation[:, :, index]
        return CAM


