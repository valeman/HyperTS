import tensorflow as tf

tf_version = str(tf.__version__)

if int(tf_version.split(".")[1]) < 11:
    from tensorflow.keras.optimizers import *
else:
    try:
        from tensorflow.keras.optimizers import *
    except:
        from tensorflow.keras.optimizers.legacy import *

from ._optimizers import AdamP
from ._optimizers import Lion

from ._optimizers import optimizer_custom_objects