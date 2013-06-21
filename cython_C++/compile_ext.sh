#/bin/bash!
export PYTHONPATH=$PYTHONPATH:/home/schm_fl/data/local-suse11-i686/lib/python2.6/site-packages
CFLAGS="-I./../../include"  \
LDFLAGS="-L./../../obj/linux-intel-gcc4/"     \
python setup.py build_ext --inplace 

