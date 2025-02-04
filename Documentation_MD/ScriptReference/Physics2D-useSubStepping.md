[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Physics2D](Physics2D.html).useSubStepping

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public static bool useSubStepping;

### Description

Whether to use simulation sub-stepping during a simulation step.

When the simulation is set to run per-frame by setting the
[Physics2D.simulationMode](Physics2D-simulationMode.html) to
[Update](SimulationMode2D.Update.html) or
[Script](SimulationMode2D.Script.html), this option will control if simulation
sub-stepping can be used.  
  
When low frame-rate conditions occur, the simulation will be simulated with
large time-steps. This results in a lower accuracy simulation. If the frame-
rate becomes too low, the simulation will begin to break down resulting in
joints being completely wrong, impulses being very large and rigidbodies
moving eratically. This situation is known as "simulation explosion" meaning
that the simulation is essentially in a failure condition which often cannot
be recovered from without the scene being reloaded, effectively resetting the
physics scene state. Obviously this should be avoided.  
  
To avoid this situation, simulation sub-stepping can be used. It achieves this
by monitoring if the frame-rate has reduced below a specified threshold
controlled by [Physics2D.minSubStepFPS](Physics2D-minSubStepFPS.html). If it
hasn't reduced below this threshold then a normal simulation step will occur.
However if it has reduced below this threshold then the physics system will
perform sub-stepping. Sub-stepping works by splitting up the current frame-
rate [delta-time](Time-deltaTime.html) into multiple sub-steps, each a higher
frequency. Doing this ensures that the physics is always simulated using a
frequency equal to or higher than the specified
[Physics2D.minSubStepFPS](Physics2D-minSubStepFPS.html). This effectively
guarantees a stable simulation.  
  
The penalty of using this feature is that sub-stepping (when the above
threshold has been exceeded) has an additional CPU costs due to the fact that
the simulation is being run multiple times although this can be reduced by not
calculating contacts for all sub-steps as controlled by
[Physics2D.useSubStepContacts](Physics2D-useSubStepContacts.html). The cost of
this should be monitored with the Unity Profiler using the Physics 2D Module.  
  
The threshold is controlled by
[Physics2D.minSubStepFPS](Physics2D-minSubStepFPS.html) and the maximum number
of sub-steps allowed is controlled by
[Physics2D.maxSubStepCount](Physics2D-maxSubStepCount.html).  
  
Additional resources:
[Physics2D.maxSubStepCount](Physics2D-maxSubStepCount.html),
[Physics2D.minSubStepFPS](Physics2D-minSubStepFPS.html),
[PhysicsScene2D.subStepCount](PhysicsScene2D-subStepCount.html) and
[PhysicsScene2D.subStepLostTime](PhysicsScene2D-subStepLostTime.html).

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

