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

**Removed**  

#  [Physics2D](Physics2D.html).autoSimulation

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

**Obsolete** Physics2D.autoSimulation is deprecated. Use
Physics2D.simulationMode instead. public static bool autoSimulation;

### Description

Set whether the physics should be simulated automatically or not.

By default, physics is updated every [Time.fixedDeltaTime](Time-
fixedDeltaTime.html) during the play mode. It happens automatically as part of
the regular game loop.  
  
However, there are cases where being able to advance physics manually is
needed. One particular example example could be networked physics where
rewinding time back and applying all the player input is required up on
receiving data from the authoritative server.  
  
To control the physics simulation manually, disable the automatic simulation
first and then use [Physics2D.Simulate](Physics2D.Simulate.html) to advance
time. Note that [MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html)
will still be called at the rate defined by [Time.fixedDeltaTime](Time-
fixedDeltaTime.html), but the physics simulation will no longer be advanced
automatically.  
  
Additional resources: [Physics2D.Simulate](Physics2D.Simulate.html).

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

