"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time
import pmt

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[]
        )

        self.message_port_register_out(pmt.intern("freq"))

        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

        self.f1_delay = 1
        self.sent_f1 = False
        self.f2_delay = 2
        self.sent_f2 = False
        self.f3_delay = 3
        self.sent_f3 = False
        self.prev_time = time.time()
        self.first_time = True

    def work(self, input_items, output_items):
        """example: multiply with constant"""


        if not self.first_time:
            if time.time() > self.prev_time + self.f1_delay and not self.sent_f1:
                self.message_port_pub(pmt.intern("freq"), pmt.to_pmt({"freq": 940000000}))
                self.sent_f1 = True
        else:
            self.message_port_pub(pmt.intern("freq"), pmt.to_pmt({"gain": 0}))
            self.first_time = False
            self.prev_time = time.time() + self.f1_delay
            self.sent_f1 = True
        if self.sent_f1 and not self.sent_f2 and time.time() > self.prev_time + self.f2_delay:
            self.message_port_pub(pmt.intern("freq"), pmt.to_pmt({"freq": 1800000000}))
            self.sent_f2 = True
        if self.sent_f1 and self.sent_f2 and not self.sent_f3 and time.time() > self.prev_time + self.f3_delay:
            self.message_port_pub(pmt.intern("freq"), pmt.to_pmt({"freq": 2630000000}))
            self.prev_time = time.time()
            self.sent_f1 = self.sent_f2 = False


        return len(input_items[0])
