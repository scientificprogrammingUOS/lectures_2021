# %load psychopy_7.py
assert '__file__' in locals()  # to make sure to not run this inside Jupyter
import psychopy
from psychopy import visual, event, core, data, logging, gui

# Store info about the experiment session
psychopyVersion = psychopy.__version__
expName = 'myexperiment'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# path for data file
filename = 'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# store general experiment information in experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

mywin = visual.Window(size=[800, 600], monitor="testMonitor", units="norm", color=[255, 255, 255])
fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0, 0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[0, 0], sf=3)
event.globalKeys.add(key='escape', func=core.quit)
# we know that stuff...

positions = [-1, -0.5, 0, 0.5, 1]

# 1 repetition of all trials, in sequential order
handler = data.TrialHandler(trialList=positions, nReps=1, method='sequential', extraInfo=expInfo)
# add trial loop to experiment
thisExp.addLoop(handler)
# go through all trials as given by the TrialHandler
for trial in handler:
    # set grating stimulus to new position
    grating.setPos([trial, 0])
    fixation.draw()
    grating.draw()
    mywin.flip()
    key = event.waitKeys()
    # log data
    handler.addData('key', key)
    # move to next row
    thisExp.nextEntry()
