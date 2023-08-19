'''
python3 paddle/check.py
'''
import paddle

print('Paddle Version: ', paddle.__version__)

print('GPU Available: ',paddle.is_compiled_with_cuda())