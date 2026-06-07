from mpf.core.mode import Mode

class MultilockManipulator(Mode):

    def mode_init(self):
        self.add_mode_event_handler(
                'set_multiball_lock_balls_to_replace',
                self.setMultiballLockBallsToReplace)  
 

    def setMultiballLockBallsToReplace(self, **kwargs):
        #self.machine.log.info("Called setMultiballLockBallsToReplace %s", kwargs['value'])
        #self.machine.log.info("Old balls to replace %i", self.machine.multiball_locks['pingine'].config['balls_to_replace'])
        self.machine.multiball_locks['left_mass_ball_lock'].config['balls_to_replace'] = kwargs['value']
        self.machine.multiball_locks['right_mass_ball_lock'].config['balls_to_replace'] = kwargs['value']
        #self.machine.log.info("New balls to replace %i", self.machine.multiball_locks['pingine'].config['balls_to_replace'])