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

#  [ComputeShader](ComputeShader.html).SetTexture

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public void SetTexture(int kernelIndex, string name, [Texture](Texture.html)
texture);

## Declaration

public void SetTexture(int kernelIndex, int nameID, [Texture](Texture.html)
texture);

## Declaration

public void SetTexture(int kernelIndex, string name, [Texture](Texture.html)
texture, int mipLevel);

## Declaration

public void SetTexture(int kernelIndex, int nameID, [Texture](Texture.html)
texture, int mipLevel);

## Declaration

public void SetTexture(int kernelIndex, string name,
[RenderTexture](RenderTexture.html) texture, int mipLevel,
[Rendering.RenderTextureSubElement](Rendering.RenderTextureSubElement.html)
element);

## Declaration

public void SetTexture(int kernelIndex, int nameID,
[RenderTexture](RenderTexture.html) texture, int mipLevel,
[Rendering.RenderTextureSubElement](Rendering.RenderTextureSubElement.html)
element);

### Parameters

kernelIndex | For which kernel the texture is being set. See [FindKernel](ComputeShader.FindKernel.html).  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
name | Name of the buffer variable in shader code.  
texture | Texture to set.  
mipLevel | Optional mipmap level of the read-write texture.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
  
### Description

Set a texture parameter.

This function can either set a regular texture that is read in the compute
shader, or an output texture that is written into by the shader. For an output
texture, it has to be a [RenderTexture](RenderTexture.html) with random write
flag enabled, see [RenderTexture.enableRandomWrite](RenderTexture-
enableRandomWrite.html).  
  
Please note that the mipLevel parameter is ignored unless the shader specifies
a read-write (unordered access) texture.  
  
Buffers and textures are set per-kernel. Use
[FindKernel](ComputeShader.FindKernel.html) to find kernel index by function
name.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data
to set from the RenderTexture. The possible options are:
[RenderTextureSubElement.Color](Rendering.RenderTextureSubElement.Color.html),
[RenderTextureSubElement.Depth](Rendering.RenderTextureSubElement.Depth.html),
and
[RenderTextureSubElement.Stencil](Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [FindKernel](ComputeShader.FindKernel.html), Additional
resources: [SetFloat](ComputeShader.SetFloat.html),
[SetFloats](ComputeShader.SetFloats.html),
[SetInt](ComputeShader.SetInt.html), [SetInts](ComputeShader.SetInts.html),
[SetBool](ComputeShader.SetBool.html),
[SetBuffer](ComputeShader.SetBuffer.html),
[SetMatrix](ComputeShader.SetMatrix.html),
[SetMatrixArray](ComputeShader.SetMatrixArray.html),
[SetVector](ComputeShader.SetVector.html),
[SetVectorArray](ComputeShader.SetVectorArray.html).,
[RenderTexture.enableRandomWrite](RenderTexture-enableRandomWrite.html),
[RenderTextureSubElement](Rendering.RenderTextureSubElement.html).

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

