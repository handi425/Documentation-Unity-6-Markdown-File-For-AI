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

# FSR2TextureTable

struct in UnityEngine.AMD

/

Implemented in:[UnityEngine.AMDModule](UnityEngine.AMDModule.html)

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

The set of texture slots available for the
[FSR2Context](AMD.FSR2Context.html). SA
[GraphicsDevice.ExecuteFSR2](AMD.GraphicsDevice.ExecuteFSR2.html).

### Properties

[biasColorMask](AMD.FSR2TextureTable-biasColorMask.html)| A mask, same size as
colorInput, preferably of format R8_UNORM that informs DLSS of possible moving
pixels. If heavy ghosting is encountered, set pixels to this mask to fix the
problem. This texture is optional.  
---|---  
[colorInput](AMD.FSR2TextureTable-colorInput.html)| The input color buffer to
upsample for FSR2Context. This texture is mandatory and you must set it to a
non-null value.  
[colorOutput](AMD.FSR2TextureTable-colorOutput.html)| The input color buffer
to upsample for FSR2Context. This texture is mandatory and you must set it to
a non-null value.  
[depth](AMD.FSR2TextureTable-depth.html)| The input depth buffer. This must be
the same size as the input color buffer. This texture is mandatory and you
must set it to a non-null value.  
[exposureTexture](AMD.FSR2TextureTable-exposureTexture.html)| A 1x1 texture
with pre-exposure values. If you do not use pre-exposure, do not set this
texture. This texture is optional.  
[motionVectors](AMD.FSR2TextureTable-motionVectors.html)| The motion vectors
requested by the FSR2Context. Depending on the AMD.FSR2FeatureFlags specified
in FSR2Context.initData, this buffer can be a smaller scale or the full output
resolution. This texture is mandatory and you must set it to a non-null value.  
[reactiveMask](AMD.FSR2TextureTable-reactiveMask.html)| Rendering mask
specifying reliance on temporal information. Additional resources: Github
documentation on reactive mask.  
[transparencyMask](AMD.FSR2TextureTable-transparencyMask.html)| A transparency
bit mask. This must be the same size as the input texture. This texture helps
the FSR2Context with ghosting issues. This texture is optional.  
  
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

