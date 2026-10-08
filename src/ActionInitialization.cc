#include "ActionInitialization.hh"

#include "DetectorConstruction.hh"
#include "PrimaryGeneratorAction.hh"
#include "RunAction.hh"
#include "EventAction.hh"
#include "TrackingAction.hh"
#include "SteppingAction.hh"
#include "StackingAction.hh"

// Master thread: only a RunAction, and no primary generator exists here
void ActionInitialization::BuildForMaster() const
{
  SetUserAction(new RunAction(fDetector, nullptr));
}

// Called once per worker thread
void ActionInitialization::Build() const
{
  PrimaryGeneratorAction* primary = new PrimaryGeneratorAction(fDetector);
  SetUserAction(primary);

  RunAction* runaction = new RunAction(fDetector, primary);
  SetUserAction(runaction);

  EventAction* eventaction = new EventAction(runaction);
  SetUserAction(eventaction);

  SetUserAction(new TrackingAction(runaction));
  SetUserAction(new SteppingAction(runaction, eventaction));
  SetUserAction(new StackingAction());
}