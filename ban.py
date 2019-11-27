import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

if len (sys.argv) == 2:
  dev = Device(host='HOSTNAME', port='PORT', user='LOGIN', passwd='PASSWORD').open()
  with Config(dev, mode='private') as cu:
    cu.load('set routing-options static route ' + sys.argv[1] + '/32 discard tag 666', format='set')
    cu.pdiff()
    cu.commit()

  dev.close()
  sys.exit(0)

else:
  exit(0)
