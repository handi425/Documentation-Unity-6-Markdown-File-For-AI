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

#  [DynamicGI](DynamicGI.html).updateThreshold

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

public static float updateThreshold;

### Description

Determines the percentage change in lighting intensity that triggers Unity to
recalculate the real-time lightmap.

Enlighten Realtime Global Illumination maintains a record of the cumulative
percentage change in lighting intensity since Unity last recalculated the
lightmaps for a Scene. When this percentage change exceeds
theDynamicGI._updateThreshold value, the Editor recalculates the lighting
solution. The default value for this property is 1%. Lower values for this
property cause the Editor to recalculate more frequently, which incurs more
CPU load. Higher values reduce the number of times Unity recalculates, and
incur less CPU load. This percentage is the maximum error tolerance before a
solve happens. Setting a positive value for this property ensures that Unity
only updates the Scene when you change the lighting. High values can cause
popping artefacts and incorrect indirect irradiance values but you can set
this property higher than 100% if you want to conserve more CPU cycles. A
value of 0 for this property causes Unity to update the real-time lightmaps
when you make even small changes to your lighting intensity. Any negative
value turns off temporal coherence, so the system will be solved every frame
even if there is no change to the lighting. Unity solves higher intensity
values less frequently than lower ones. This is because humans perceive
differences in low intensity lights more than differences in high intensity
ones.

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

