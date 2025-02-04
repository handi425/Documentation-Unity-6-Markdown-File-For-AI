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

# TextureFormat

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

Format used when creating textures from scripts.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a new alpha-only texture and assign it
            // to the renderer's material
            [Texture2D](Texture2D.html) texture = new [Texture2D](Texture2D.html)(128, 128, [TextureFormat.Alpha8](TextureFormat.Alpha8.html), false);
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;
        }
    }
    

Note that not all graphics cards support all texture formats, use
[SystemInfo.SupportsTextureFormat](SystemInfo.SupportsTextureFormat.html) to
check. Also, only the [Texture2D](Texture2D.html) class supports texture
creation from script with Crunch compression texture formats.  
  
Additional resources: [Texture2D](Texture2D.html), [texture
assets](../Manual/Textures.html).

### Properties

[Alpha8](TextureFormat.Alpha8.html)| Alpha-only texture format, 8 bit integer.  
---|---  
[ARGB4444](TextureFormat.ARGB4444.html)| A 16 bits/pixel texture format.
Texture stores color with an alpha channel.  
[RGB24](TextureFormat.RGB24.html)| Three channel (RGB) texture format, 8-bits
unsigned integer per channel.  
[RGBA32](TextureFormat.RGBA32.html)| Four channel (RGBA) texture format,
8-bits unsigned integer per channel.  
[ARGB32](TextureFormat.ARGB32.html)| Color with alpha texture format, 8-bits
per channel.  
[RGB565](TextureFormat.RGB565.html)| A 16 bit color texture format.  
[R16](TextureFormat.R16.html)| Single channel (R) texture format, 16-bits
unsigned integer.  
[DXT1](TextureFormat.DXT1.html)| Compressed color texture format.  
[DXT5](TextureFormat.DXT5.html)| Compressed color with alpha channel texture
format.  
[RGBA4444](TextureFormat.RGBA4444.html)| Color and alpha texture format, 4 bit
per channel.  
[BGRA32](TextureFormat.BGRA32.html)| Color with alpha texture format, 8-bits
per channel.  
[RHalf](TextureFormat.RHalf.html)| Scalar (R) texture format, 16 bit floating
point.  
[RGHalf](TextureFormat.RGHalf.html)| Two color (RG) texture format, 16 bit
floating point per channel.  
[RGBAHalf](TextureFormat.RGBAHalf.html)| RGB color and alpha texture format,
16 bit floating point per channel.  
[RFloat](TextureFormat.RFloat.html)| Scalar (R) texture format, 32 bit
floating point.  
[RGFloat](TextureFormat.RGFloat.html)| Two color (RG) texture format, 32 bit
floating point per channel.  
[RGBAFloat](TextureFormat.RGBAFloat.html)| RGB color and alpha texture format,
32-bit floats per channel.  
[YUY2](TextureFormat.YUY2.html)| A format that uses the YUV color space and is
often used for video encoding or playback.  
[RGB9e5Float](TextureFormat.RGB9e5Float.html)| RGB HDR format, with 9 bit
mantissa per channel and a 5 bit shared exponent.  
[BC4](TextureFormat.BC4.html)| Compressed one channel (R) texture format.  
[BC5](TextureFormat.BC5.html)| Compressed two-channel (RG) texture format.  
[BC6H](TextureFormat.BC6H.html)| HDR compressed color texture format.  
[BC7](TextureFormat.BC7.html)| High quality compressed color texture format.  
[DXT1Crunched](TextureFormat.DXT1Crunched.html)| Compressed color texture
format with Crunch compression for smaller storage sizes.  
[DXT5Crunched](TextureFormat.DXT5Crunched.html)| Compressed color with alpha
channel texture format with Crunch compression for smaller storage sizes.  
[PVRTC_RGB2](TextureFormat.PVRTC_RGB2.html)| PowerVR (iOS) 2 bits/pixel
compressed color texture format.  
[PVRTC_RGBA2](TextureFormat.PVRTC_RGBA2.html)| PowerVR (iOS) 2 bits/pixel
compressed with alpha channel texture format.  
[PVRTC_RGB4](TextureFormat.PVRTC_RGB4.html)| PowerVR (iOS) 4 bits/pixel
compressed color texture format.  
[PVRTC_RGBA4](TextureFormat.PVRTC_RGBA4.html)| PowerVR (iOS) 4 bits/pixel
compressed with alpha channel texture format.  
[ETC_RGB4](TextureFormat.ETC_RGB4.html)| ETC (GLES2.0) 4 bits/pixel compressed
RGB texture format.  
[EAC_R](TextureFormat.EAC_R.html)| ETC2 / EAC (GL ES 3.0) 4 bits/pixel
compressed unsigned single-channel texture format.  
[EAC_R_SIGNED](TextureFormat.EAC_R_SIGNED.html)| ETC2 / EAC (GL ES 3.0) 4
bits/pixel compressed signed single-channel texture format.  
[EAC_RG](TextureFormat.EAC_RG.html)| ETC2 / EAC (GL ES 3.0) 8 bits/pixel
compressed unsigned dual-channel (RG) texture format.  
[EAC_RG_SIGNED](TextureFormat.EAC_RG_SIGNED.html)| ETC2 / EAC (GL ES 3.0) 8
bits/pixel compressed signed dual-channel (RG) texture format.  
[ETC2_RGB](TextureFormat.ETC2_RGB.html)| ETC2 (GL ES 3.0) 4 bits/pixel
compressed RGB texture format.  
[ETC2_RGBA1](TextureFormat.ETC2_RGBA1.html)| ETC2 (GL ES 3.0) 4 bits/pixel
RGB+1-bit alpha texture format.  
[ETC2_RGBA8](TextureFormat.ETC2_RGBA8.html)| ETC2 (GL ES 3.0) 8 bits/pixel
compressed RGBA texture format.  
[ASTC_4x4](TextureFormat.ASTC_4x4.html)| ASTC (4x4 pixel block in 128 bits)
compressed RGB(A) texture format.  
[ASTC_5x5](TextureFormat.ASTC_5x5.html)| ASTC (5x5 pixel block in 128 bits)
compressed RGB(A) texture format.  
[ASTC_6x6](TextureFormat.ASTC_6x6.html)| ASTC (6x6 pixel block in 128 bits)
compressed RGB(A) texture format.  
[ASTC_8x8](TextureFormat.ASTC_8x8.html)| ASTC (8x8 pixel block in 128 bits)
compressed RGB(A) texture format.  
[ASTC_10x10](TextureFormat.ASTC_10x10.html)| ASTC (10x10 pixel block in 128
bits) compressed RGB(A) texture format.  
[ASTC_12x12](TextureFormat.ASTC_12x12.html)| ASTC (12x12 pixel block in 128
bits) compressed RGB(A) texture format.  
[RG16](TextureFormat.RG16.html)| Two channel (RG) texture format, 8-bits
unsigned integer per channel.  
[R8](TextureFormat.R8.html)| Single channel (R) texture format, 8-bits
unsigned integer.  
[ETC_RGB4Crunched](TextureFormat.ETC_RGB4Crunched.html)| Compressed color
texture format with Crunch compression for smaller storage sizes.  
[ETC2_RGBA8Crunched](TextureFormat.ETC2_RGBA8Crunched.html)| Compressed color
with alpha channel texture format using Crunch compression for smaller storage
sizes.  
[ASTC_HDR_4x4](TextureFormat.ASTC_HDR_4x4.html)| ASTC (4x4 pixel block in 128
bits) compressed RGB(A) HDR texture format.  
[ASTC_HDR_5x5](TextureFormat.ASTC_HDR_5x5.html)| ASTC (5x5 pixel block in 128
bits) compressed RGB(A) HDR texture format.  
[ASTC_HDR_6x6](TextureFormat.ASTC_HDR_6x6.html)| ASTC (6x6 pixel block in 128
bits) compressed RGB(A) HDR texture format.  
[ASTC_HDR_8x8](TextureFormat.ASTC_HDR_8x8.html)| ASTC (8x8 pixel block in 128
bits) compressed RGB(A) texture format.  
[ASTC_HDR_10x10](TextureFormat.ASTC_HDR_10x10.html)| ASTC (10x10 pixel block
in 128 bits) compressed RGB(A) HDR texture format.  
[ASTC_HDR_12x12](TextureFormat.ASTC_HDR_12x12.html)| ASTC (12x12 pixel block
in 128 bits) compressed RGB(A) HDR texture format.  
[RG32](TextureFormat.RG32.html)| Two channel (RG) texture format, 16-bits
unsigned integer per channel.  
[RGB48](TextureFormat.RGB48.html)| Three channel (RGB) texture format, 16-bits
unsigned integer per channel.  
[RGBA64](TextureFormat.RGBA64.html)| Four channel (RGBA) texture format,
16-bits unsigned integer per channel.  
[R8_SIGNED](TextureFormat.R8_SIGNED.html)| Single channel (R) texture format,
8-bits signed integer.  
[RG16_SIGNED](TextureFormat.RG16_SIGNED.html)| Two channel (RG) texture
format, 8-bits signed integer per channel.  
[RGB24_SIGNED](TextureFormat.RGB24_SIGNED.html)| Three channel (RGB) texture
format, 8-bits signed integer per channel.  
[RGBA32_SIGNED](TextureFormat.RGBA32_SIGNED.html)| Four channel (RGBA) texture
format, 8-bits signed integer per channel.  
[R16_SIGNED](TextureFormat.R16_SIGNED.html)| Single channel (R) texture
format, 16-bits signed integer.  
[RG32_SIGNED](TextureFormat.RG32_SIGNED.html)| Two channel (RG) texture
format, 16-bits signed integer per channel.  
[RGB48_SIGNED](TextureFormat.RGB48_SIGNED.html)| Three color (RGB) texture
format, 16-bits signed integer per channel.  
[RGBA64_SIGNED](TextureFormat.RGBA64_SIGNED.html)| Four channel (RGBA) texture
format, 16-bits signed integer per channel.  
  
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

