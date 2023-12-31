import appdaemon.plugins.hass.hassapi as hass


LIGHT_SEQUENCE = 'LIGHT_SEQUENCE'


class LightSequence(hass.Hass):
    
    # register callbacks
    def initialize(self):
        self.log("Lights started")
        self.sequence_handle = None
        self.listen_event(self.lights_cb, LIGHT_SEQUENCE)


    def lights_cb(self, event, data, kwargs):
        """
        A callback for the LIGHT_SEQUENCE event. It checks if there is a handle for the run_sequence method, if None
        it creates a new handle by running the sequence, if not None, it cancels the previous handle before running a 
        new sequence
        """
        if self.sequence_handle is None:
            self.sequence_handle = self.run_sequence('sequence.office_on')
        else:
            self.cancel_timer(self.sequence_handle)
            self.sequence_handle = self.run_sequence('sequence.office_on')
       