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

# ReflectionProbeTimeSlicingMode

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

When a probe's [ReflectionProbe.refreshMode](ReflectionProbe-refreshMode.html)
is set to
[ReflectionProbeRefreshMode.EveryFrame](Rendering.ReflectionProbeRefreshMode.EveryFrame.html),
this enum specify whether or not Unity should update the probe's cubemap over
several frames or update the whole cubemap in one frame. Updating a probe's
cubemap is a costly operation. Unity needs to render the entire Scene for each
face of the cubemap, as well as perform special blurring in order to get
glossy reflections. The impact on frame rate can be significant. Time-slicing
helps maintaning a more constant frame rate during these updates by performing
the rendering over several frames.

### Properties

[AllFacesAtOnce](Rendering.ReflectionProbeTimeSlicingMode.AllFacesAtOnce.html)|
Instructs Unity to use time-slicing by first rendering all faces at once, then
spreading the remaining work over the next 8 frames. Using this option,
updating the probe will take 9 frames.  
---|---  
[IndividualFaces](Rendering.ReflectionProbeTimeSlicingMode.IndividualFaces.html)|
Instructs Unity to spread the rendering of each face over several frames.
Using this option, updating the cubemap will take 14 frames. This option
greatly reduces the impact on frame rate, however it may produce incorrect
results, especially in Scenes where lighting conditions change over these 14
frames.  
[NoTimeSlicing](Rendering.ReflectionProbeTimeSlicingMode.NoTimeSlicing.html)|
Unity will render the probe entirely in one frame.  
  
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

