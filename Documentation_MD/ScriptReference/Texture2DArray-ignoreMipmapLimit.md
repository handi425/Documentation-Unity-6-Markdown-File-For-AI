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

#  [Texture2DArray](Texture2DArray.html).ignoreMipmapLimit

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

[Switch to Manual](../Manual/class-Texture2DArray.html "Go to Texture2DArray
Component in the Manual")

public bool ignoreMipmapLimit;

### Description

This property causes a texture to ignore all texture mipmap limit settings.

When this property is `true`, Unity always uploads the texture to the GPU at
full resolution, disregarding the active quality setting's global texture
mipmap limit and texture mipmap limit group settings, even if this texture has
a texture mipmap limit group set.  
  
When this property is `false`, the texture respects the active quality
setting's global texture mipmap limit, unless the texture is part of a
[mipmapLimitGroup](Texture2DArray-mipmapLimitGroup.html).  
  
When changing this property at runtime: if this causes the actual mipmap limit
for this texture to change, then the texture will be reuploaded to the GPU.
For an optimal workflow, set this property in the constructor or in the
texture importer to immediately upload the texture with the currently active
mipmap limits properly applied or ignored. If the texture has no mipmaps, this
property has no effect. Note that this can only be toggled at runtime if the
Texture is [readable](Texture-isReadable.html). By default, this property is
set to `true` when created in a script, which means all mipmap levels are
uploaded.  
  
Additional resources: [TextureImporter.ignoreMipmapLimit](TextureImporter-
ignoreMipmapLimit.html), [MipmapLimitDescriptor](MipmapLimitDescriptor.html),
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

