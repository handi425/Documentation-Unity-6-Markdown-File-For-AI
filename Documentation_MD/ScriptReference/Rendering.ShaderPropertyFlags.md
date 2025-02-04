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

# ShaderPropertyFlags

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

Flags that control how a shader property behaves.

When the Unity Editor compiles a ShaderLab script, it assigns shader property
flags to its shader properties based on the attributes you assign to those
properties. For example, if you add the "[HideInInspector]" attribute to a
shader property declaration, Unity sets the
[HideInInspector](Rendering.ShaderPropertyFlags.HideInInspector.html) flag
when it compiles the script. If you add more than one attribute to a property,
the Editor combines the flags using a bitwise OR operation.

### Properties

[None](Rendering.ShaderPropertyFlags.None.html)| No flags are set.  
---|---  
[HideInInspector](Rendering.ShaderPropertyFlags.HideInInspector.html)|
Signifies that Unity hides the property in the default Material Inspector.  
[PerRendererData](Rendering.ShaderPropertyFlags.PerRendererData.html)| In the
Material Inspector, Unity queries the value for this property from the
Renderer's MaterialPropertyBlock, instead of from the Material. The value will
also appear as read-only.  
[NoScaleOffset](Rendering.ShaderPropertyFlags.NoScaleOffset.html)| Do not show
UV scale/offset fields next to Textures in the default Material Inspector.  
[Normal](Rendering.ShaderPropertyFlags.Normal.html)| Signifies that values of
this property contain Normal (normalized vector) data.  
[HDR](Rendering.ShaderPropertyFlags.HDR.html)| Signifies that values of this
property contain High Dynamic Range (HDR) data.  
[Gamma](Rendering.ShaderPropertyFlags.Gamma.html)| Signifies that values of
this property are in gamma space. If the active color space is linear, Unity
converts the values to linear space values.  
[NonModifiableTextureData](Rendering.ShaderPropertyFlags.NonModifiableTextureData.html)|
You cannot edit this Texture property in the default Material Inspector.  
[MainTexture](Rendering.ShaderPropertyFlags.MainTexture.html)| Signifies that
value of this property contains the main texture of the Material.  
[MainColor](Rendering.ShaderPropertyFlags.MainColor.html)| Signifies that
value of this property contains the main color of the Material.  
  
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

