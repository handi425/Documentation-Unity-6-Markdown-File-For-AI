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

# DLSSTextureTable

struct in UnityEngine.NVIDIA

/

Implemented in:[UnityEngine.NVIDIAModule](UnityEngine.NVIDIAModule.html)

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
[DLSSContext](NVIDIA.DLSSContext.html). SA
[GraphicsDevice.ExecuteDLSS](NVIDIA.GraphicsDevice.ExecuteDLSS.html)

### Properties

[biasColorMask](NVIDIA.DLSSTextureTable-biasColorMask.html)| A mask, same size
as colorInput, preferably of format R8_UNORM that informs DLSS of possible
moving pixels. If heavy ghosting is encountered, set pixels to this mask to
fix the problem. This texture is optional.  
---|---  
[colorInput](NVIDIA.DLSSTextureTable-colorInput.html)| The input color buffer
to upsample for DLSSContext. This texture is mandatory and you must set it to
a non-null value.  
[colorOutput](NVIDIA.DLSSTextureTable-colorOutput.html)| The output color
buffer to write the upsampling result for DLSSContext. This must be large
enough to fit in the output rect specified in the command. This texture is
mandatory and you must set it to a non-null value.  
[depth](NVIDIA.DLSSTextureTable-depth.html)| The input depth buffer. This must
be the same size as the input color buffer. This texture is mandatory and you
must set it to a non-null value.  
[exposureTexture](NVIDIA.DLSSTextureTable-exposureTexture.html)| A 1x1 texture
with pre-exposure values. If you do not use pre-exposure, do not set this
texture. This texture is optional.  
[motionVectors](NVIDIA.DLSSTextureTable-motionVectors.html)| The motion
vectors requested by the DLSSContext. Depending on the DLSSFeatureFlags
specified in DLSSContext.initData, this buffer can be a smaller scale or the
full output resolution. This texture is mandatory and you must set it to a
non-null value.  
[transparencyMask](NVIDIA.DLSSTextureTable-transparencyMask.html)| A
transparency bit mask. This must be the same size as the input texture. This
texture helps the DLSSContext with ghosting issues. This texture is optional.  
  
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

