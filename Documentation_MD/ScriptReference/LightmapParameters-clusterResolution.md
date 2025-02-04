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

#  [LightmapParameters](LightmapParameters.html).clusterResolution

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

[Switch to Manual](../Manual/class-LightmapParameters.html "Go to
LightmapParameters Component in the Manual")

public float clusterResolution;

### Description

Controls the resolution at which Enlighten Realtime Global Illumination stores
and can transfer input light.

Typically this resolution can be slightly lower than the resolution of the
real-time lightmap without significantly reducing the final quality, although
this depends on the kinds of lighting environments you wish to use. Small,
bright light sources will require a higher clusterResolution for Enlighten
Realtime Global Illumination to capture them accurately.  
  
  
  
Cluster resolution is multiplied by the real-time lightmap resolution. A high
value means a higher cluster resolution. A value of 1 matches each texel in
the real-time lightmap with one input cluster.  
  
  
  
Using a very small cluster resolution results in light being smeared across
the output texels. Larger values do not significantly increase quality (as
they have to be averaged for the final output texel), but can cause
unnecessary increases in time and memory footprint.

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

