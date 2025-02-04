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

#  [DynamicGI](DynamicGI.html).materialUpdateTimeSlice

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

public static int materialUpdateTimeSlice;

### Description

The number of milliseconds that can be spent on material updates.

Material updates render albedo and emissive textures per system on the GPU,
read them back and pass the buffers to Enlighten Realtime Global Illumination.
This happens automatically for all the new systems when a scene is loaded. The
timeslice amount limits how much time is spent on those steps on the main
thread in each frame.  
  
Material updates are processed one system at a time until the timeslice amount
is reached/exceeded. The granularity is of one system, so it is possible that
material updates will take more than the timeslice amount.  
  
Minimum value: 0. If there are any scheduled material updates in the current
frame, only one system will be processed.  
Maximum value: Int32.MaxValue. All the scheduled material updates will be
processed in one go. Restores the pre-2017.2 behaviour.  
Default value: 8 milliseconds.

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

