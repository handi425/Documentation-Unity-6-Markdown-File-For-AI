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

#  [ParticleSystem](ParticleSystem.html).Simulate

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

## Declaration

public void Simulate(float t);

## Declaration

public void Simulate(float t, bool withChildren = true);

## Declaration

public void Simulate(float t, bool withChildren = true, bool restart = true);

## Declaration

public void Simulate(float t, bool withChildren = true, bool restart = true,
bool fixedTimeStep = true);

### Parameters

t | Time period in seconds to advance the ParticleSystem simulation by. If `restart` is true, the ParticleSystem will be reset to 0 time, and then advanced by this value. If `restart` is false, the ParticleSystem simulation will be advanced in time from its current state by this value.  
---|---  
withChildren | Fast-forward all child Particle Systems as well.  
restart | Restart and start from the beginning.  
fixedTimeStep | Only update the system at fixed intervals, based on the value in "Fixed Time" in the Time options.  
  
### Description

Fast-forwards the Particle System by simulating particles over the given
period of time, then pauses it.

Additional resources: [Play](ParticleSystem.Play.html),
[Pause](ParticleSystem.Pause.html) functions.

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

