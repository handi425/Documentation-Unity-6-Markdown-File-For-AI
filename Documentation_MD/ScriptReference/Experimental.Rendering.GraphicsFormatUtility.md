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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# GraphicsFormatUtility

class in UnityEngine.Experimental.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

This utility class contains helper functions that enable you to query
properties of a [TextureFormat](TextureFormat.html),
[RenderTextureFormat](RenderTextureFormat.html), or
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html). This class also
includes format conversion and size calculation functions.

### Static Methods

[ComputeMipChainSize](Experimental.Rendering.GraphicsFormatUtility.ComputeMipChainSize.html)|
Computes the memory size in bytes for a chain of mipmaps.  
---|---  
[ComputeMipmapSize](Experimental.Rendering.GraphicsFormatUtility.ComputeMipmapSize.html)|
Computes the memory size in bytes for a single mipmap.  
[ConvertToAlphaFormat](Experimental.Rendering.GraphicsFormatUtility.ConvertToAlphaFormat.html)|
Input a GraphicsFormat to return an equivalent GraphicsFormat that includes an
alpha component.  
[GetAlphaComponentCount](Experimental.Rendering.GraphicsFormatUtility.GetAlphaComponentCount.html)|
Returns the number of alpha components of the format.  
[GetBlockHeight](Experimental.Rendering.GraphicsFormatUtility.GetBlockHeight.html)|
Returns the height in texels of a texel block.  
[GetBlockSize](Experimental.Rendering.GraphicsFormatUtility.GetBlockSize.html)|
Returns the memory size in bytes of a texel block.  
[GetBlockWidth](Experimental.Rendering.GraphicsFormatUtility.GetBlockWidth.html)|
Returns the width in texels of a texel block.  
[GetColorComponentCount](Experimental.Rendering.GraphicsFormatUtility.GetColorComponentCount.html)|
Returns the number of color components of the format.  
[GetComponentCount](Experimental.Rendering.GraphicsFormatUtility.GetComponentCount.html)|
Returns the number of components this format has.  
[GetDepthBits](Experimental.Rendering.GraphicsFormatUtility.GetDepthBits.html)|
Returns the number of bits per pixel this format contains for depth.  
[GetDepthStencilFormat](Experimental.Rendering.GraphicsFormatUtility.GetDepthStencilFormat.html)|
Returns a supported depth stencil format that has 'minimumDepthBits' of bits
or higher per pixel for the depth component if a compatible format exists on
the current platform. If 'minimumStencilBits' is higher than 0, and a
compatible format exists on the current platform, Unity returns a depth
stencil format with 8 bits per pixel for the stencil component.  
[GetFormatString](Experimental.Rendering.GraphicsFormatUtility.GetFormatString.html)|
Returns a string that represents a format enum value.  
[GetGraphicsFormat](Experimental.Rendering.GraphicsFormatUtility.GetGraphicsFormat.html)|
Translates RenderTextureFormat or TextureFormat into GraphicsFormat.  
[GetLinearFormat](Experimental.Rendering.GraphicsFormatUtility.GetLinearFormat.html)|
Returns the equivalent linear format of a GraphicsFormat. For example, this
function returns kFormatR8G8B8A8_UNorm if the input is kFormatR8G8B8A8_SRGB.
If the input GraphicsFormat is already linear, this function returns the input
GraphicsFormat.  
[GetRenderTextureFormat](Experimental.Rendering.GraphicsFormatUtility.GetRenderTextureFormat.html)|
Translates GraphicsFormat into RenderTextureFormat.  
[GetSRGBFormat](Experimental.Rendering.GraphicsFormatUtility.GetSRGBFormat.html)|
Returns the equivalent sRGB format of a GraphicsFormat. For example, this
function returns kFormatR8G8B8A8_SRGB if the input is kFormatR8G8B8A8_UNorm.
If the input GraphicsFormat is already sRGB, this function returns the input
GraphicsFormat. If there is no equivalent sRGB format, this function returns
the input GraphicsFormat.  
[GetSwizzleA](Experimental.Rendering.GraphicsFormatUtility.GetSwizzleA.html)|
Returns a FormatSwizzle enum that is mapped to the alpha channel for a given
format.  
[GetSwizzleB](Experimental.Rendering.GraphicsFormatUtility.GetSwizzleB.html)|
Returns a FormatSwizzle enum that is mapped to the blue channel for a given
format.  
[GetSwizzleG](Experimental.Rendering.GraphicsFormatUtility.GetSwizzleG.html)|
Returns a FormatSwizzle enum that is mapped to the green channel for a given
format.  
[GetSwizzleR](Experimental.Rendering.GraphicsFormatUtility.GetSwizzleR.html)|
Returns FormatSwizzle enum of which channel is mapped to the R channel for a
given format.  
[GetTextureFormat](Experimental.Rendering.GraphicsFormatUtility.GetTextureFormat.html)|
Translates GraphicsFormat into TextureFormat.  
[HasAlphaChannel](Experimental.Rendering.GraphicsFormatUtility.HasAlphaChannel.html)|
Returns true if the format has an alpha component. Returns false otherwise.  
[Is16BitPackedFormat](Experimental.Rendering.GraphicsFormatUtility.Is16BitPackedFormat.html)|
Returns true if the format is packed and a 16-bit format. Returns false
otherwise.  
[IsAlphaOnlyFormat](Experimental.Rendering.GraphicsFormatUtility.IsAlphaOnlyFormat.html)|
Returns true if the format only has an alpha component. Returns false
otherwise.  
[IsAlphaTestFormat](Experimental.Rendering.GraphicsFormatUtility.IsAlphaTestFormat.html)|
Returns true if the format has an alpha component with only 1 or 2 bits.
Returns false otherwise.  
[IsASTCFormat](Experimental.Rendering.GraphicsFormatUtility.IsASTCFormat.html)|
Returns true if the format uses ASTC. Returns false otherwise.  
[IsBCFormat](Experimental.Rendering.GraphicsFormatUtility.IsBCFormat.html)|
Returns true if the format is a DXTC, RGTC or BPTC format. Returns false
otherwise.  
[IsBPTCFormat](Experimental.Rendering.GraphicsFormatUtility.IsBPTCFormat.html)|
Returns true if the format uses BPTC. Returns false otherwise.  
[IsCompressedFormat](Experimental.Rendering.GraphicsFormatUtility.IsCompressedFormat.html)|
Returns true if the format is compressed. Returns false otherwise.  
[IsCrunchFormat](Experimental.Rendering.GraphicsFormatUtility.IsCrunchFormat.html)|
Returns true if the format data is compressed with Crunch. Returns false
otherwise.  
[IsDepthFormat](Experimental.Rendering.GraphicsFormatUtility.IsDepthFormat.html)|
Returns true if the format is a depth format. Returns false otherwise.  
[IsDepthStencilFormat](Experimental.Rendering.GraphicsFormatUtility.IsDepthStencilFormat.html)|
Returns true if the format is a depth or stencil format. Returns false
otherwise.  
[IsDXTCFormat](Experimental.Rendering.GraphicsFormatUtility.IsDXTCFormat.html)|
Returns true if the format uses DXTC. Returns false otherwise.  
[IsEACFormat](Experimental.Rendering.GraphicsFormatUtility.IsEACFormat.html)|
Returns true if the format uses EAC. Returns false otherwise.  
[IsETCFormat](Experimental.Rendering.GraphicsFormatUtility.IsETCFormat.html)|
Returns true if the format uses ETC and ETC2. Returns false otherwise.  
[IsFloatFormat](Experimental.Rendering.GraphicsFormatUtility.IsFloatFormat.html)|
Returns true if the format is a single precision floating point format.
Returns false otherwise.  
[IsHalfFormat](Experimental.Rendering.GraphicsFormatUtility.IsHalfFormat.html)|
Returns true if the format is a half precision floating point format. Returns
false otherwise.  
[IsHDRFormat](Experimental.Rendering.GraphicsFormatUtility.IsHDRFormat.html)|
Returns true if the format is capable of representing HDR data. Returns false
otherwise.  
[IsIEEE754Format](Experimental.Rendering.GraphicsFormatUtility.IsIEEE754Format.html)|
Returns true if the format is a floating point format. Returns false
otherwise.  
[IsIntegerFormat](Experimental.Rendering.GraphicsFormatUtility.IsIntegerFormat.html)|
Returns true if the format is an integer format. Returns false otherwise.  
[IsNormFormat](Experimental.Rendering.GraphicsFormatUtility.IsNormFormat.html)|
Returns true if the format is a normalized format. Returns false otherwise.  
[IsPackedFormat](Experimental.Rendering.GraphicsFormatUtility.IsPackedFormat.html)|
Returns true if the format is packed. Returns false otherwise.  
[IsPVRTCFormat](Experimental.Rendering.GraphicsFormatUtility.IsPVRTCFormat.html)|
Returns true if the format uses PVRTC. Returns false otherwise.  
[IsRGTCFormat](Experimental.Rendering.GraphicsFormatUtility.IsRGTCFormat.html)|
Returns true if the format uses RGTC. Returns false otherwise.  
[IsSignedFormat](Experimental.Rendering.GraphicsFormatUtility.IsSignedFormat.html)|
Returns true if the format is a signed format. Returns false otherwise.  
[IsSIntFormat](Experimental.Rendering.GraphicsFormatUtility.IsSIntFormat.html)|
Returns true if the format is a signed and integer format. Returns false
otherwise.  
[IsSNormFormat](Experimental.Rendering.GraphicsFormatUtility.IsSNormFormat.html)|
Returns true if the format is a signed normalized format. Returns false
otherwise.  
[IsSRGBFormat](Experimental.Rendering.GraphicsFormatUtility.IsSRGBFormat.html)|
Returns true if the format performs sRGB to linear on read and linear to sRGB
on write. Returns false otherwise.  
[IsStencilFormat](Experimental.Rendering.GraphicsFormatUtility.IsStencilFormat.html)|
Returns true if the format is a stencil format. Returns false otherwise.  
[IsSwizzleFormat](Experimental.Rendering.GraphicsFormatUtility.IsSwizzleFormat.html)|
Returns true if the format is not a RGBA format. Returns false otherwise.  
[IsUIntFormat](Experimental.Rendering.GraphicsFormatUtility.IsUIntFormat.html)|
Returns true if the format is an unsigned and integer format. Returns false
otherwise.  
[IsUNormFormat](Experimental.Rendering.GraphicsFormatUtility.IsUNormFormat.html)|
Returns true if the format is an unsigned normalized format. Returns false
otherwise.  
[IsUnsignedFormat](Experimental.Rendering.GraphicsFormatUtility.IsUnsignedFormat.html)|
Returns true if the format is an unsigned format. Returns false otherwise.  
[IsXRFormat](Experimental.Rendering.GraphicsFormatUtility.IsXRFormat.html)|
Returns true if the format is an extended range format. With extended range
format, the blue, green, and red components are linearly encoded, and their
values range from -0.752941 to 1.25098. The alpha component is always clamped
to a [0.0, 1.0] range in sampling, rendering, and writing operations, despite
supporting values outside this range. Returns false otherwise.  
  
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

