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

# AntiAliasingSamples

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

[Switch to Manual](../Manual/class-LightmapParameters.html "Go to
LightmapParameters Component in the Manual")

### Description

The number of sub-texel positions to use when sampling a lightmap texel.

The number of sub-texel positions to use when sampling a lightmap texel.
Values higher than 1 will use supersampling to improve lightmap quality and
reduce artifacts related to aliasing.  
  
  
  
The default value of 4 should be sufficient to remove the majority of aliasing
issues. However, in some cases it may be necessary to increase the number of
sub-texel sample positions. This can be particularly useful where "jaggy"
edges in direct lighting can be observed. Typically this is more visible when
using baked shadows.  
  
  
  
Note that memory usage increases proportionally to the number of samples used.
Using high values in large Scenes may therefore increase the chance that
lightmap bakes do not complete, especially when using large lightmap texture
sizes.  
  
Additional resources:
[LightmapParameters.antiAliasingSamples](LightmapParameters-
antiAliasingSamples.html).

### Properties

[SSAA1](LightmapParameters.AntiAliasingSamples.SSAA1.html)| Disables
supersampling. This results in a faster but lower-quality bake.  
---|---  
[SSAA4](LightmapParameters.AntiAliasingSamples.SSAA4.html)| Supersamples each
texel by a factor of 4. This results in a 4 times larger G-buffer size.  
[SSAA16](LightmapParameters.AntiAliasingSamples.SSAA16.html)| Supersamples
each texel by a factor of 16. This results in a 16 times larger G-buffer size.  
  
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

