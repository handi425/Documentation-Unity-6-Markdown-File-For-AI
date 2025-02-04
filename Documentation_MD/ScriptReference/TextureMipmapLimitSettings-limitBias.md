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

#  [TextureMipmapLimitSettings](TextureMipmapLimitSettings.html).limitBias

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

public int limitBias;

### Description

The new value to apply on top of the global texture mipmap limit. Can act as
an offset (default) or an override to it.

By default, this is equal to `0`.  
  
If [limitBiasMode](TextureMipmapLimitSettings-limitBiasMode.html) is set to
[TextureMipmapLimitBiasMode.OffsetGlobalLimit](TextureMipmapLimitBiasMode.OffsetGlobalLimit.html),
`limitBias` acts as an offset to the current quality level's
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html). For example, if the global texture mipmap
limit is `1` (half size) and `limitBias` is also `1`, the final combined value
for textures that are affected by these settings is `2`. (quarter size)  
  
If [limitBiasMode](TextureMipmapLimitSettings-limitBiasMode.html) is set to
[TextureMipmapLimitBiasMode.OverrideGlobalLimit](TextureMipmapLimitBiasMode.OverrideGlobalLimit.html),
`limitBias` ignores the global texture mipmap limit and acts as an override.
For example, if [QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) is `2` (quarter size), and `limitBias` is `0`
(full resolution), the final combined value for textures that are affected by
these settings is `0` (full resolution).  
  
Additional resources: [limitBiasMode](TextureMipmapLimitSettings-
limitBiasMode.html),
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html).

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

