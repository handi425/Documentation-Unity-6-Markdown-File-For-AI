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

# RealtimeGICPUUsage

enumeration

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

### Description

How much CPU usage to assign to the final lighting calculations at runtime.

How many CPU worker threads to create for Enlighten Realtime Global
Illumination lighting calculations in the Player. Increasing this makes the
system react faster to changes in lighting at a cost of using more CPU time.
The higher the CPU Usage value, the more worker threads are created for
solving Enlighten Realtime Global Illumination.  
  
**Please note** that some platforms will allow all CPUs to be occupied by
worker threads whilst some have a max limit:  
**Android:** If the device is a bigLittle architecture, only the little CPUs
will be used, otherwise it is CPUs - 1.  

### Properties

[Low](Rendering.RealtimeGICPUUsage.Low.html)| 25% of the allowed CPU threads
are used as worker threads.  
---|---  
[Medium](Rendering.RealtimeGICPUUsage.Medium.html)| 50% of the allowed CPU
threads are used as worker threads.  
[High](Rendering.RealtimeGICPUUsage.High.html)| 75% of the allowed CPU threads
are used as worker threads.  
[Unlimited](Rendering.RealtimeGICPUUsage.Unlimited.html)| 100% of the allowed
CPU threads are used as worker threads.  
  
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

