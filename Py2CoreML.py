import argparse

import coremltools
from keras.models import load_model

'''
TODO
Batch conversion
from model
'''

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='file to convert to Apple CoreML model')
parser.add_argument('--name', help='name to give to the coreML model file')
args = parser.parse_args()

coremlName = args.name
filename = args.source
print (args.source, args.name)
model = load_model(filepath=args.source)
coreml_model = coremltools.converters.keras.convert(model)
coreml_model.save(coremlName + '.mlmodel')
