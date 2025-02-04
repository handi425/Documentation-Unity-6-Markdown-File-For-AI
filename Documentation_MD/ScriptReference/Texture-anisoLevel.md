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

#  [Texture](Texture.html).anisoLevel

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

public int anisoLevel;

### Description

Defines the anisotropic filtering level of the Texture.

Anisotropic filtering makes Textures look better when viewed at a shallow
angle, but it can be slower to process on the GPU. Anisotropic filtering is
commonly used to improve the appearance of floor, ground or road Textures.  
  
The value range of this variable is 0 to 16. A value of 1 equals no filtering
applied and 16 equals full filtering applied. As the value gets bigger, the
Texture is clearer at shallow angles. Lower values mean the Texture is more
blurry at shallow angles.  
  
When the `anisoLevel` value is 0 and in **Quality Settings** , **Anisotropic
Filtering** is set to **Forced On** , Unity does not apply anisotropic
filtering. You can use this to disable anisotropic filtering for a Texture
that would behave unpredictably with anisotropic filtering applied.  
  
When the `anisoLevel` value is between 1 and 9, and in **Quality Settings** ,
**Anisotropic Filtering** is set to **Forced On** , Unity sets the
`anisoLevel` to 9. If the value is higher than 9, Unity clamps it between 9
and 16.  
  
If you use the Metal, Vulkan and OpenGL APIs, you can control mipmap filtering
and anisotropic filtering levels independently. When you enable anisotropic
filtering in any other graphics APIs, Unity also enables trilinear filtering.  
  
Additional resources: [Texture assets](../Manual/Textures.html).

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

