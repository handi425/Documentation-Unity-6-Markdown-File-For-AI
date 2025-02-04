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

#  [Physics2D](Physics2D.html).minSubStepFPS

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

public static float minSubStepFPS;

### Description

The minimum FPS allowed for a simulation step before sub-stepping will be
used.

When simulation sub-stepping is enabled with
[Physics2D.useSubStepping](Physics2D-useSubStepping.html), this property is
used as a FPS threshold below which simulation sub-stepping will occur.
Specifically, when the current frame-rate is lower than this value, simulation
sub-stepping will occur.  
  
This value should be set to the frame-rate you expect your simulation to start
performing poorly. Unfortunately this has to be determined on a project-by-
project basis because it depends on the complexity of the simulation
components used and their configuration. A good rule of thumb here though is
that as frame-rates reduce to less than 30 FPS, any simulation would be
extremely approximate but some projects are still fine even at these low
frequencies. The cost of this should be monitored with the Unity Profiler
using the Physics 2D Module.  
  
Additional resources:
[Physics2D.useSubStepping](Physics2D-useSubStepping.html),
[Physics2D.maxSubStepCount](Physics2D-maxSubStepCount.html),
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

