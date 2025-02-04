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

# GraphicsFormat

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

Use this format to create either Textures or RenderTextures from scripts.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        TextureCreationFlags flags;
        void Start()
        {
            // Create a new texture and assign it to the material of the renderer.
            var texture = new [Texture2D](Texture2D.html)(128, 128, [GraphicsFormat.R8G8B8A8_SRGB](Experimental.Rendering.GraphicsFormat.R8G8B8A8_SRGB.html), flags);
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;
        }
    }
    

Each graphics card may not support all usages across formats. Use
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) to check
which usages the graphics card supports.  
  
Each "format" is represented by a single enum value. The name of a format is
based on the following criteria:

  * For color formats, the component-format specifies the size of the R, G, B, and A components (if present).
  * For depth/stencil formats, the component-format specifies the size of the depth (D) and stencil (S) components (if present).
  * UNorm: The components are unsigned normalized values in the range [0,1].
  * SNorm: The components are signed normalized values in the range [-1,1].
  * UInt: The components are unsigned integer values in the range [0, 2^(n-1)].
  * SInt: The components are signed integer values in the range [-2^(n-1),2^(n-1)-1].
  * UFloat: The components are unsigned floating-point numbers (used by packed, shared exponent, and some compressed formats).
  * SFloat: The components are signed floating-point numbers.
  * SRGB: The R, G, and B components are unsigned normalized values that represent values using sRGB nonlinear encoding, while the A component (if one exists) is a regular unsigned normalized value.
  * PACKnn: The format is packed into an underlying type with nn bits.

Additional resources: [Texture2D](Texture2D.html), [texture
assets](../Manual/Textures.html).

### Properties

[None](Experimental.Rendering.GraphicsFormat.None.html)| The format is not
specified.  
---|---  
[R8_SRGB](Experimental.Rendering.GraphicsFormat.R8_SRGB.html)| A one-
component, 8-bit unsigned normalized format that has a single 8-bit R
component stored with sRGB nonlinear encoding.  
[R8G8_SRGB](Experimental.Rendering.GraphicsFormat.R8G8_SRGB.html)| A two-
component, 16-bit unsigned normalized format that has an 8-bit R component
stored with sRGB nonlinear encoding in byte 0, and an 8-bit G component stored
with sRGB nonlinear encoding in byte 1.  
[R8G8B8_SRGB](Experimental.Rendering.GraphicsFormat.R8G8B8_SRGB.html)| A
three-component, 24-bit unsigned normalized format that has an 8-bit R
component stored with sRGB nonlinear encoding in byte 0, an 8-bit G component
stored with sRGB nonlinear encoding in byte 1, and an 8-bit B component stored
with sRGB nonlinear encoding in byte 2.  
[R8G8B8A8_SRGB](Experimental.Rendering.GraphicsFormat.R8G8B8A8_SRGB.html)| A
four-component, 32-bit unsigned normalized format that has an 8-bit R
component stored with sRGB nonlinear encoding in byte 0, an 8-bit G component
stored with sRGB nonlinear encoding in byte 1, an 8-bit B component stored
with sRGB nonlinear encoding in byte 2, and an 8-bit A component in byte 3.  
[R8_UNorm](Experimental.Rendering.GraphicsFormat.R8_UNorm.html)| A one-
component, 8-bit unsigned normalized format that has a single 8-bit R
component.  
[R8G8_UNorm](Experimental.Rendering.GraphicsFormat.R8G8_UNorm.html)| A two-
component, 16-bit unsigned normalized format that has an 8-bit R component
stored with sRGB nonlinear encoding in byte 0, and an 8-bit G component stored
with sRGB nonlinear encoding in byte 1.  
[R8G8B8_UNorm](Experimental.Rendering.GraphicsFormat.R8G8B8_UNorm.html)| A
three-component, 24-bit unsigned normalized format that has an 8-bit R
component in byte 0, an 8-bit G component in byte 1, and an 8-bit B component
in byte 2.  
[R8G8B8A8_UNorm](Experimental.Rendering.GraphicsFormat.R8G8B8A8_UNorm.html)| A
four-component, 32-bit unsigned normalized format that has an 8-bit R
component in byte 0, an 8-bit G component in byte 1, an 8-bit B component in
byte 2, and an 8-bit A component in byte 3.  
[R8_SNorm](Experimental.Rendering.GraphicsFormat.R8_SNorm.html)| A one-
component, 8-bit signed normalized format that has a single 8-bit R component.  
[R8G8_SNorm](Experimental.Rendering.GraphicsFormat.R8G8_SNorm.html)| A two-
component, 16-bit signed normalized format that has an 8-bit R component
stored with sRGB nonlinear encoding in byte 0, and an 8-bit G component stored
with sRGB nonlinear encoding in byte 1.  
[R8G8B8_SNorm](Experimental.Rendering.GraphicsFormat.R8G8B8_SNorm.html)| A
three-component, 24-bit signed normalized format that has an 8-bit R component
in byte 0, an 8-bit G component in byte 1, and an 8-bit B component in byte 2.  
[R8G8B8A8_SNorm](Experimental.Rendering.GraphicsFormat.R8G8B8A8_SNorm.html)| A
four-component, 32-bit signed normalized format that has an 8-bit R component
in byte 0, an 8-bit G component in byte 1, an 8-bit B component in byte 2, and
an 8-bit A component in byte 3.  
[R8_UInt](Experimental.Rendering.GraphicsFormat.R8_UInt.html)| A one-
component, 8-bit unsigned integer format that has a single 8-bit R component.  
[R8G8_UInt](Experimental.Rendering.GraphicsFormat.R8G8_UInt.html)| A two-
component, 16-bit unsigned integer format that has an 8-bit R component in
byte 0, and an 8-bit G component in byte 1.  
[R8G8B8_UInt](Experimental.Rendering.GraphicsFormat.R8G8B8_UInt.html)| A
three-component, 24-bit unsigned integer format that has an 8-bit R component
in byte 0, an 8-bit G component in byte 1, and an 8-bit B component in byte 2.  
[R8G8B8A8_UInt](Experimental.Rendering.GraphicsFormat.R8G8B8A8_UInt.html)| A
four-component, 32-bit unsigned integer format that has an 8-bit R component
in byte 0, an 8-bit G component in byte 1, an 8-bit B component in byte 2, and
an 8-bit A component in byte 3.  
[R8_SInt](Experimental.Rendering.GraphicsFormat.R8_SInt.html)| A one-
component, 8-bit signed integer format that has a single 8-bit R component.  
[R8G8_SInt](Experimental.Rendering.GraphicsFormat.R8G8_SInt.html)| A two-
component, 16-bit signed integer format that has an 8-bit R component in byte
0, and an 8-bit G component in byte 1.  
[R8G8B8_SInt](Experimental.Rendering.GraphicsFormat.R8G8B8_SInt.html)| A
three-component, 24-bit signed integer format that has an 8-bit R component in
byte 0, an 8-bit G component in byte 1, and an 8-bit B component in byte 2.  
[R8G8B8A8_SInt](Experimental.Rendering.GraphicsFormat.R8G8B8A8_SInt.html)| A
four-component, 32-bit signed integer format that has an 8-bit R component in
byte 0, an 8-bit G component in byte 1, an 8-bit B component in byte 2, and an
8-bit A component in byte 3.  
[R16_UNorm](Experimental.Rendering.GraphicsFormat.R16_UNorm.html)| A one-
component, 16-bit unsigned normalized format that has a single 16-bit R
component.  
[R16G16_UNorm](Experimental.Rendering.GraphicsFormat.R16G16_UNorm.html)| A
two-component, 32-bit unsigned normalized format that has a 16-bit R component
in bytes 0..1, and a 16-bit G component in bytes 2..3.  
[R16G16B16_UNorm](Experimental.Rendering.GraphicsFormat.R16G16B16_UNorm.html)|
A three-component, 48-bit unsigned normalized format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, and a 16-bit B
component in bytes 4..5.  
[R16G16B16A16_UNorm](Experimental.Rendering.GraphicsFormat.R16G16B16A16_UNorm.html)|
A four-component, 64-bit unsigned normalized format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, a 16-bit B
component in bytes 4..5, and a 16-bit A component in bytes 6..7.  
[R16_SNorm](Experimental.Rendering.GraphicsFormat.R16_SNorm.html)| A one-
component, 16-bit signed normalized format that has a single 16-bit R
component.  
[R16G16_SNorm](Experimental.Rendering.GraphicsFormat.R16G16_SNorm.html)| A
two-component, 32-bit signed normalized format that has a 16-bit R component
in bytes 0..1, and a 16-bit G component in bytes 2..3.  
[R16G16B16_SNorm](Experimental.Rendering.GraphicsFormat.R16G16B16_SNorm.html)|
A three-component, 48-bit signed normalized format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, and a 16-bit B
component in bytes 4..5.  
[R16G16B16A16_SNorm](Experimental.Rendering.GraphicsFormat.R16G16B16A16_SNorm.html)|
A four-component, 64-bit signed normalized format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, a 16-bit B
component in bytes 4..5, and a 16-bit A component in bytes 6..7.  
[R16_UInt](Experimental.Rendering.GraphicsFormat.R16_UInt.html)| A one-
component, 16-bit unsigned integer format that has a single 16-bit R
component.  
[R16G16_UInt](Experimental.Rendering.GraphicsFormat.R16G16_UInt.html)| A two-
component, 32-bit unsigned integer format that has a 16-bit R component in
bytes 0..1, and a 16-bit G component in bytes 2..3.  
[R16G16B16_UInt](Experimental.Rendering.GraphicsFormat.R16G16B16_UInt.html)| A
three-component, 48-bit unsigned integer format that has a 16-bit R component
in bytes 0..1, a 16-bit G component in bytes 2..3, and a 16-bit B component in
bytes 4..5.  
[R16G16B16A16_UInt](Experimental.Rendering.GraphicsFormat.R16G16B16A16_UInt.html)|
A four-component, 64-bit unsigned integer format that has a 16-bit R component
in bytes 0..1, a 16-bit G component in bytes 2..3, a 16-bit B component in
bytes 4..5, and a 16-bit A component in bytes 6..7.  
[R16_SInt](Experimental.Rendering.GraphicsFormat.R16_SInt.html)| A one-
component, 16-bit signed integer format that has a single 16-bit R component.  
[R16G16_SInt](Experimental.Rendering.GraphicsFormat.R16G16_SInt.html)| A two-
component, 32-bit signed integer format that has a 16-bit R component in bytes
0..1, and a 16-bit G component in bytes 2..3.  
[R16G16B16_SInt](Experimental.Rendering.GraphicsFormat.R16G16B16_SInt.html)| A
three-component, 48-bit signed integer format that has a 16-bit R component in
bytes 0..1, a 16-bit G component in bytes 2..3, and a 16-bit B component in
bytes 4..5.  
[R16G16B16A16_SInt](Experimental.Rendering.GraphicsFormat.R16G16B16A16_SInt.html)|
A four-component, 64-bit signed integer format that has a 16-bit R component
in bytes 0..1, a 16-bit G component in bytes 2..3, a 16-bit B component in
bytes 4..5, and a 16-bit A component in bytes 6..7.  
[R32_UInt](Experimental.Rendering.GraphicsFormat.R32_UInt.html)| A one-
component, 32-bit unsigned integer format that has a single 32-bit R
component.  
[R32G32_UInt](Experimental.Rendering.GraphicsFormat.R32G32_UInt.html)| A two-
component, 64-bit unsigned integer format that has a 32-bit R component in
bytes 0..3, and a 32-bit G component in bytes 4..7.  
[R32G32B32_UInt](Experimental.Rendering.GraphicsFormat.R32G32B32_UInt.html)| A
three-component, 96-bit unsigned integer format that has a 32-bit R component
in bytes 0..3, a 32-bit G component in bytes 4..7, and a 32-bit B component in
bytes 8..11.  
[R32G32B32A32_UInt](Experimental.Rendering.GraphicsFormat.R32G32B32A32_UInt.html)|
A four-component, 128-bit unsigned integer format that has a 32-bit R
component in bytes 0..3, a 32-bit G component in bytes 4..7, a 32-bit B
component in bytes 8..11, and a 32-bit A component in bytes 12..15.  
[R32_SInt](Experimental.Rendering.GraphicsFormat.R32_SInt.html)| A one-
component, 32-bit signed integer format that has a single 32-bit R component.  
[R32G32_SInt](Experimental.Rendering.GraphicsFormat.R32G32_SInt.html)| A two-
component, 64-bit signed integer format that has a 32-bit R component in bytes
0..3, and a 32-bit G component in bytes 4..7.  
[R32G32B32_SInt](Experimental.Rendering.GraphicsFormat.R32G32B32_SInt.html)| A
three-component, 96-bit signed integer format that has a 32-bit R component in
bytes 0..3, a 32-bit G component in bytes 4..7, and a 32-bit B component in
bytes 8..11.  
[R32G32B32A32_SInt](Experimental.Rendering.GraphicsFormat.R32G32B32A32_SInt.html)|
A four-component, 128-bit signed integer format that has a 32-bit R component
in bytes 0..3, a 32-bit G component in bytes 4..7, a 32-bit B component in
bytes 8..11, and a 32-bit A component in bytes 12..15.  
[R16_SFloat](Experimental.Rendering.GraphicsFormat.R16_SFloat.html)| A one-
component, 16-bit signed floating-point format that has a single 16-bit R
component.  
[R16G16_SFloat](Experimental.Rendering.GraphicsFormat.R16G16_SFloat.html)| A
two-component, 32-bit signed floating-point format that has a 16-bit R
component in bytes 0..1, and a 16-bit G component in bytes 2..3.  
[R16G16B16_SFloat](Experimental.Rendering.GraphicsFormat.R16G16B16_SFloat.html)|
A three-component, 48-bit signed floating-point format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, and a 16-bit B
component in bytes 4..5.  
[R16G16B16A16_SFloat](Experimental.Rendering.GraphicsFormat.R16G16B16A16_SFloat.html)|
A four-component, 64-bit signed floating-point format that has a 16-bit R
component in bytes 0..1, a 16-bit G component in bytes 2..3, a 16-bit B
component in bytes 4..5, and a 16-bit A component in bytes 6..7.  
[R32_SFloat](Experimental.Rendering.GraphicsFormat.R32_SFloat.html)| A one-
component, 32-bit signed floating-point format that has a single 32-bit R
component.  
[R32G32_SFloat](Experimental.Rendering.GraphicsFormat.R32G32_SFloat.html)| A
two-component, 64-bit signed floating-point format that has a 32-bit R
component in bytes 0..3, and a 32-bit G component in bytes 4..7.  
[R32G32B32_SFloat](Experimental.Rendering.GraphicsFormat.R32G32B32_SFloat.html)|
A three-component, 96-bit signed floating-point format that has a 32-bit R
component in bytes 0..3, a 32-bit G component in bytes 4..7, and a 32-bit B
component in bytes 8..11.  
[R32G32B32A32_SFloat](Experimental.Rendering.GraphicsFormat.R32G32B32A32_SFloat.html)|
A four-component, 128-bit signed floating-point format that has a 32-bit R
component in bytes 0..3, a 32-bit G component in bytes 4..7, a 32-bit B
component in bytes 8..11, and a 32-bit A component in bytes 12..15.  
[B8G8R8_SRGB](Experimental.Rendering.GraphicsFormat.B8G8R8_SRGB.html)| A
three-component, 24-bit unsigned normalized format that has an 8-bit B
component stored with sRGB nonlinear encoding in byte 0, an 8-bit G component
stored with sRGB nonlinear encoding in byte 1, and an 8-bit R component stored
with sRGB nonlinear encoding in byte 2.  
[B8G8R8A8_SRGB](Experimental.Rendering.GraphicsFormat.B8G8R8A8_SRGB.html)| A
four-component, 32-bit unsigned normalized format that has an 8-bit B
component stored with sRGB nonlinear encoding in byte 0, an 8-bit G component
stored with sRGB nonlinear encoding in byte 1, an 8-bit R component stored
with sRGB nonlinear encoding in byte 2, and an 8-bit A component in byte 3.  
[B8G8R8_UNorm](Experimental.Rendering.GraphicsFormat.B8G8R8_UNorm.html)| A
three-component, 24-bit unsigned normalized format that has an 8-bit B
component in byte 0, an 8-bit G component in byte 1, and an 8-bit R component
in byte 2.  
[B8G8R8A8_UNorm](Experimental.Rendering.GraphicsFormat.B8G8R8A8_UNorm.html)| A
four-component, 32-bit unsigned normalized format that has an 8-bit B
component in byte 0, an 8-bit G component in byte 1, an 8-bit R component in
byte 2, and an 8-bit A component in byte 3.  
[B8G8R8_SNorm](Experimental.Rendering.GraphicsFormat.B8G8R8_SNorm.html)| A
three-component, 24-bit signed normalized format that has an 8-bit B component
in byte 0, an 8-bit G component in byte 1, and an 8-bit R component in byte 2.  
[B8G8R8A8_SNorm](Experimental.Rendering.GraphicsFormat.B8G8R8A8_SNorm.html)| A
four-component, 32-bit signed normalized format that has an 8-bit B component
in byte 0, an 8-bit G component in byte 1, an 8-bit R component in byte 2, and
an 8-bit A component in byte 3.  
[B8G8R8_UInt](Experimental.Rendering.GraphicsFormat.B8G8R8_UInt.html)| A
three-component, 24-bit unsigned integer format that has an 8-bit B component
in byte 0, an 8-bit G component in byte 1, and an 8-bit R component in byte 2  
[B8G8R8A8_UInt](Experimental.Rendering.GraphicsFormat.B8G8R8A8_UInt.html)| A
four-component, 32-bit unsigned integer format that has an 8-bit B component
in byte 0, an 8-bit G component in byte 1, an 8-bit R component in byte 2, and
an 8-bit A component in byte 3.  
[B8G8R8_SInt](Experimental.Rendering.GraphicsFormat.B8G8R8_SInt.html)| A
three-component, 24-bit signed integer format that has an 8-bit B component in
byte 0, an 8-bit G component in byte 1, and an 8-bit R component in byte 2.  
[B8G8R8A8_SInt](Experimental.Rendering.GraphicsFormat.B8G8R8A8_SInt.html)| A
four-component, 32-bit signed integer format that has an 8-bit B component in
byte 0, an 8-bit G component in byte 1, an 8-bit R component in byte 2, and an
8-bit A component in byte 3.  
[R4G4B4A4_UNormPack16](Experimental.Rendering.GraphicsFormat.R4G4B4A4_UNormPack16.html)|
A four-component, 16-bit packed unsigned normalized format that has a 4-bit R
component in bits 12..15, a 4-bit G component in bits 8..11, a 4-bit B
component in bits 4..7, and a 4-bit A component in bits 0..3.  
[B4G4R4A4_UNormPack16](Experimental.Rendering.GraphicsFormat.B4G4R4A4_UNormPack16.html)|
A four-component, 16-bit packed unsigned normalized format that has a 4-bit B
component in bits 12..15, a 4-bit G component in bits 8..11, a 4-bit R
component in bits 4..7, and a 4-bit A component in bits 0..3.  
[R5G6B5_UNormPack16](Experimental.Rendering.GraphicsFormat.R5G6B5_UNormPack16.html)|
A three-component, 16-bit packed unsigned normalized format that has a 5-bit R
component in bits 11..15, a 6-bit G component in bits 5..10, and a 5-bit B
component in bits 0..4.  
[B5G6R5_UNormPack16](Experimental.Rendering.GraphicsFormat.B5G6R5_UNormPack16.html)|
A three-component, 16-bit packed unsigned normalized format that has a 5-bit B
component in bits 11..15, a 6-bit G component in bits 5..10, and a 5-bit R
component in bits 0..4.  
[R5G5B5A1_UNormPack16](Experimental.Rendering.GraphicsFormat.R5G5B5A1_UNormPack16.html)|
A four-component, 16-bit packed unsigned normalized format that has a 5-bit R
component in bits 11..15, a 5-bit G component in bits 6..10, a 5-bit B
component in bits 1..5, and a 1-bit A component in bit 0.  
[B5G5R5A1_UNormPack16](Experimental.Rendering.GraphicsFormat.B5G5R5A1_UNormPack16.html)|
A four-component, 16-bit packed unsigned normalized format that has a 5-bit B
component in bits 11..15, a 5-bit G component in bits 6..10, a 5-bit R
component in bits 1..5, and a 1-bit A component in bit 0.  
[A1R5G5B5_UNormPack16](Experimental.Rendering.GraphicsFormat.A1R5G5B5_UNormPack16.html)|
A four-component, 16-bit packed unsigned normalized format that has a 1-bit A
component in bit 15, a 5-bit R component in bits 10..14, a 5-bit G component
in bits 5..9, and a 5-bit B component in bits 0..4.  
[E5B9G9R9_UFloatPack32](Experimental.Rendering.GraphicsFormat.E5B9G9R9_UFloatPack32.html)|
A three-component, 32-bit packed unsigned floating-point format that has a
5-bit shared exponent in bits 27..31, a 9-bit B component mantissa in bits
18..26, a 9-bit G component mantissa in bits 9..17, and a 9-bit R component
mantissa in bits 0..8.  
[B10G11R11_UFloatPack32](Experimental.Rendering.GraphicsFormat.B10G11R11_UFloatPack32.html)|
A three-component, 32-bit packed unsigned floating-point format that has a
10-bit B component in bits 22..31, an 11-bit G component in bits 11..21, an
11-bit R component in bits 0..10.  
[A2B10G10R10_UNormPack32](Experimental.Rendering.GraphicsFormat.A2B10G10R10_UNormPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 2-bit A
component in bits 30..31, a 10-bit B component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit R component in bits 0..9.  
[A2B10G10R10_UIntPack32](Experimental.Rendering.GraphicsFormat.A2B10G10R10_UIntPack32.html)|
A four-component, 32-bit packed unsigned integer format that has a 2-bit A
component in bits 30..31, a 10-bit B component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit R component in bits 0..9.  
[A2B10G10R10_SIntPack32](Experimental.Rendering.GraphicsFormat.A2B10G10R10_SIntPack32.html)|
A four-component, 32-bit packed signed integer format that has a 2-bit A
component in bits 30..31, a 10-bit B component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit R component in bits 0..9.  
[A2R10G10B10_UNormPack32](Experimental.Rendering.GraphicsFormat.A2R10G10B10_UNormPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 2-bit A
component in bits 30..31, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9.  
[A2R10G10B10_UIntPack32](Experimental.Rendering.GraphicsFormat.A2R10G10B10_UIntPack32.html)|
A four-component, 32-bit packed unsigned integer format that has a 2-bit A
component in bits 30..31, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9.  
[A2R10G10B10_SIntPack32](Experimental.Rendering.GraphicsFormat.A2R10G10B10_SIntPack32.html)|
A four-component, 32-bit packed signed integer format that has a 2-bit A
component in bits 30..31, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9.  
[A2R10G10B10_XRSRGBPack32](Experimental.Rendering.GraphicsFormat.A2R10G10B10_XRSRGBPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 2-bit A
component in bits 30..31, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9. The
components are gamma encoded and their values range from -0.5271 to 1.66894.
The alpha component is clamped to either 0.0 or 1.0 on sampling, rendering,
and writing operations.  
[A2R10G10B10_XRUNormPack32](Experimental.Rendering.GraphicsFormat.A2R10G10B10_XRUNormPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 2-bit A
component in bits 30..31, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9. The
components are linearly encoded and their values range from -0.752941 to
1.25098 (pre-expansion). The alpha component is clamped to either 0.0 or 1.0
on sampling, rendering, and writing operations.  
[R10G10B10_XRSRGBPack32](Experimental.Rendering.GraphicsFormat.R10G10B10_XRSRGBPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 10-bit R
component in bits 20..29, a 10-bit G component in bits 10..19, and a 10-bit B
component in bits 0..9. The components are gamma encoded and their values
range from -0.5271 to 1.66894. The alpha component is clamped to either 0.0 or
1.0 on sampling, rendering, and writing operations.  
[R10G10B10_XRUNormPack32](Experimental.Rendering.GraphicsFormat.R10G10B10_XRUNormPack32.html)|
A four-component, 32-bit packed unsigned normalized format that has a 10-bit R
component in bits 20..29, a 10-bit G component in bits 10..19, and a 10-bit B
component in bits 0..9. The components are linearly encoded and their values
range from -0.752941 to 1.25098 (pre-expansion).  
[A10R10G10B10_XRSRGBPack32](Experimental.Rendering.GraphicsFormat.A10R10G10B10_XRSRGBPack32.html)|
A four-component, 64-bit packed unsigned normalized format that has a 10-bit A
component in bits 30..39, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9. The
components are gamma encoded and their values range from -0.5271 to 1.66894.
The alpha component is clamped to either 0.0 or 1.0 on sampling, rendering,
and writing operations.  
[A10R10G10B10_XRUNormPack32](Experimental.Rendering.GraphicsFormat.A10R10G10B10_XRUNormPack32.html)|
A four-component, 64-bit packed unsigned normalized format that has a 10-bit A
component in bits 30..39, a 10-bit R component in bits 20..29, a 10-bit G
component in bits 10..19, and a 10-bit B component in bits 0..9. The
components are linearly encoded and their values range from -0.752941 to
1.25098 (pre-expansion). The alpha component is clamped to either 0.0 or 1.0
on sampling, rendering, and writing operations.  
[D16_UNorm](Experimental.Rendering.GraphicsFormat.D16_UNorm.html)| A one-
component, 16-bit unsigned normalized format that has a single 16-bit depth
component.  
[D24_UNorm](Experimental.Rendering.GraphicsFormat.D24_UNorm.html)| A two-
component, 32-bit format that has 24 unsigned normalized bits in the depth
component and, optionally: 8 bits that are unused.  
[D24_UNorm_S8_UInt](Experimental.Rendering.GraphicsFormat.D24_UNorm_S8_UInt.html)|
A two-component, 32-bit packed format that has 8 unsigned integer bits in the
stencil component, and 24 unsigned normalized bits in the depth component.  
[D32_SFloat](Experimental.Rendering.GraphicsFormat.D32_SFloat.html)| A one-
component, 32-bit signed floating-point format that has 32-bits in the depth
component.  
[D32_SFloat_S8_UInt](Experimental.Rendering.GraphicsFormat.D32_SFloat_S8_UInt.html)|
A two-component format that has 32 signed float bits in the depth component
and 8 unsigned integer bits in the stencil component. There are optionally:
24-bits that are unused.  
[S8_UInt](Experimental.Rendering.GraphicsFormat.S8_UInt.html)| A one-
component, 8-bit unsigned integer format that has 8-bits in the stencil
component.  
[RGBA_DXT1_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_DXT1_SRGB.html)| A
three-component, block-compressed format (also known as BC1). Each 64-bit
compressed texel block encodes a 4×4 rectangle of unsigned normalized RGB
texel data with sRGB nonlinear encoding. This format has a 1 bit alpha
channel.  
[RGBA_DXT1_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_DXT1_UNorm.html)|
A three-component, block-compressed format (also known as BC1). Each 64-bit
compressed texel block encodes a 4×4 rectangle of unsigned normalized RGB
texel data. This format has a 1 bit alpha channel.  
[RGBA_DXT3_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_DXT3_SRGB.html)| A
four-component, block-compressed format (also known as BC2) where each 128-bit
compressed texel block encodes a 4×4 rectangle of unsigned normalized RGBA
texel data with the first 64 bits encoding alpha values followed by 64 bits
encoding RGB values with sRGB nonlinear encoding.  
[RGBA_DXT3_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_DXT3_UNorm.html)|
A four-component, block-compressed format (also known as BC2) where each
128-bit compressed texel block encodes a 4×4 rectangle of unsigned normalized
RGBA texel data with the first 64 bits encoding alpha values followed by 64
bits encoding RGB values.  
[RGBA_DXT5_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_DXT5_SRGB.html)| A
four-component, block-compressed format (also known as BC3) where each 128-bit
compressed texel block encodes a 4×4 rectangle of unsigned normalized RGBA
texel data with the first 64 bits encoding alpha values followed by 64 bits
encoding RGB values with sRGB nonlinear encoding.  
[RGBA_DXT5_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_DXT5_UNorm.html)|
A four-component, block-compressed format (also known as BC3) where each
128-bit compressed texel block encodes a 4×4 rectangle of unsigned normalized
RGBA texel data with the first 64 bits encoding alpha values followed by 64
bits encoding RGB values.  
[R_BC4_UNorm](Experimental.Rendering.GraphicsFormat.R_BC4_UNorm.html)| A one-
component, block-compressed format where each 64-bit compressed texel block
encodes a 4×4 rectangle of unsigned normalized red texel data.  
[R_BC4_SNorm](Experimental.Rendering.GraphicsFormat.R_BC4_SNorm.html)| A one-
component, block-compressed format where each 64-bit compressed texel block
encodes a 4×4 rectangle of signed normalized red texel data.  
[RG_BC5_UNorm](Experimental.Rendering.GraphicsFormat.RG_BC5_UNorm.html)| A
two-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RG texel data with the
first 64 bits encoding red values followed by 64 bits encoding green values.  
[RG_BC5_SNorm](Experimental.Rendering.GraphicsFormat.RG_BC5_SNorm.html)| A
two-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of signed normalized RG texel data with the
first 64 bits encoding red values followed by 64 bits encoding green values.  
[RGB_BC6H_UFloat](Experimental.Rendering.GraphicsFormat.RGB_BC6H_UFloat.html)|
A three-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned floating-point RGB texel data.  
[RGB_BC6H_SFloat](Experimental.Rendering.GraphicsFormat.RGB_BC6H_SFloat.html)|
A three-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of signed floating-point RGB texel data.  
[RGBA_BC7_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_BC7_SRGB.html)| A
four-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with sRGB
nonlinear encoding applied to the RGB components.  
[RGBA_BC7_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_BC7_UNorm.html)| A
four-component, block-compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data.  
[RGB_PVRTC_2Bpp_SRGB](Experimental.Rendering.GraphicsFormat.RGB_PVRTC_2Bpp_SRGB.html)|
A three-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 8×4 rectangle of unsigned normalized RGB texel data with sRGB
nonlinear encoding. This format has no alpha and is considered opaque.  
[RGB_PVRTC_2Bpp_UNorm](Experimental.Rendering.GraphicsFormat.RGB_PVRTC_2Bpp_UNorm.html)|
A three-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 8×4 rectangle of unsigned normalized RGB texel data. This
format has no alpha and is considered opaque.  
[RGB_PVRTC_4Bpp_SRGB](Experimental.Rendering.GraphicsFormat.RGB_PVRTC_4Bpp_SRGB.html)|
A three-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data with sRGB
nonlinear encoding. This format has no alpha and is considered opaque.  
[RGB_PVRTC_4Bpp_UNorm](Experimental.Rendering.GraphicsFormat.RGB_PVRTC_4Bpp_UNorm.html)|
A three-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data. This
format has no alpha and is considered opaque.  
[RGBA_PVRTC_2Bpp_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_PVRTC_2Bpp_SRGB.html)|
A four-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 8×4 rectangle of unsigned normalized RGBA texel data with the
first 32 bits encoding alpha values followed by 32 bits encoding RGB values
with sRGB nonlinear encoding applied.  
[RGBA_PVRTC_2Bpp_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_PVRTC_2Bpp_UNorm.html)|
A four-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 8×4 rectangle of unsigned normalized RGBA texel data with the
first 32 bits encoding alpha values followed by 32 bits encoding RGB values.  
[RGBA_PVRTC_4Bpp_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_PVRTC_4Bpp_SRGB.html)|
A four-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with the
first 32 bits encoding alpha values followed by 32 bits encoding RGB values
with sRGB nonlinear encoding applied.  
[RGBA_PVRTC_4Bpp_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_PVRTC_4Bpp_UNorm.html)|
A four-component, PVRTC compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with the
first 32 bits encoding alpha values followed by 32 bits encoding RGB values.  
[RGB_ETC_UNorm](Experimental.Rendering.GraphicsFormat.RGB_ETC_UNorm.html)| A
three-component, ETC compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data. This
format has no alpha and is considered opaque.  
[RGB_ETC2_SRGB](Experimental.Rendering.GraphicsFormat.RGB_ETC2_SRGB.html)| A
three-component, ETC2 compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data with sRGB
nonlinear encoding. This format has no alpha and is considered opaque.  
[RGB_ETC2_UNorm](Experimental.Rendering.GraphicsFormat.RGB_ETC2_UNorm.html)| A
three-component, ETC2 compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data. This
format has no alpha and is considered opaque.  
[RGB_A1_ETC2_SRGB](Experimental.Rendering.GraphicsFormat.RGB_A1_ETC2_SRGB.html)|
A four-component, ETC2 compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data with sRGB
nonlinear encoding, and provides 1 bit of alpha.  
[RGB_A1_ETC2_UNorm](Experimental.Rendering.GraphicsFormat.RGB_A1_ETC2_UNorm.html)|
A four-component, ETC2 compressed format where each 64-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGB texel data, and
provides 1 bit of alpha.  
[RGBA_ETC2_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ETC2_SRGB.html)| A
four-component, ETC2 compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with the
first 64 bits encoding alpha values followed by 64 bits encoding RGB values
with sRGB nonlinear encoding applied.  
[RGBA_ETC2_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ETC2_UNorm.html)|
A four-component, ETC2 compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with the
first 64 bits encoding alpha values followed by 64 bits encoding RGB values.  
[R_EAC_UNorm](Experimental.Rendering.GraphicsFormat.R_EAC_UNorm.html)| A one-
component, ETC2 compressed format where each 64-bit compressed texel block
encodes a 4×4 rectangle of unsigned normalized red texel data.  
[R_EAC_SNorm](Experimental.Rendering.GraphicsFormat.R_EAC_SNorm.html)| A one-
component, ETC2 compressed format where each 64-bit compressed texel block
encodes a 4×4 rectangle of signed normalized red texel data.  
[RG_EAC_UNorm](Experimental.Rendering.GraphicsFormat.RG_EAC_UNorm.html)| A
two-component, ETC2 compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RG texel data with the
first 64 bits encoding red values followed by 64 bits encoding green values.  
[RG_EAC_SNorm](Experimental.Rendering.GraphicsFormat.RG_EAC_SNorm.html)| A
two-component, ETC2 compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of signed normalized RG texel data with the
first 64 bits encoding red values followed by 64 bits encoding green values.  
[RGBA_ASTC4X4_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC4X4_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data with sRGB
nonlinear encoding applied to the RGB components.  
[RGBA_ASTC4X4_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC4X4_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of unsigned normalized RGBA texel data.  
[RGBA_ASTC5X5_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC5X5_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 5×5 rectangle of unsigned normalized RGBA texel data with sRGB
nonlinear encoding applied to the RGB components.  
[RGBA_ASTC5X5_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC5X5_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 5×5 rectangle of unsigned normalized RGBA texel data.  
[RGBA_ASTC6X6_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC6X6_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 6×6 rectangle of unsigned normalized RGBA texel data with sRGB
nonlinear encoding applied to the RGB components.  
[RGBA_ASTC6X6_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC6X6_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 6×6 rectangle of unsigned normalized RGBA texel data.  
[RGBA_ASTC8X8_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC8X8_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes an 8×8 rectangle of unsigned normalized RGBA texel data with
sRGB nonlinear encoding applied to the RGB components.  
[RGBA_ASTC8X8_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC8X8_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes an 8×8 rectangle of unsigned normalized RGBA texel data.  
[RGBA_ASTC10X10_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC10X10_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 10×10 rectangle of unsigned normalized RGBA texel data with
sRGB nonlinear encoding applied to the RGB components.  
[RGBA_ASTC10X10_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC10X10_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 10×10 rectangle of unsigned normalized RGBA texel data.  
[RGBA_ASTC12X12_SRGB](Experimental.Rendering.GraphicsFormat.RGBA_ASTC12X12_SRGB.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 12×12 rectangle of unsigned normalized RGBA texel data with
sRGB nonlinear encoding applied to the RGB components.  
[RGBA_ASTC12X12_UNorm](Experimental.Rendering.GraphicsFormat.RGBA_ASTC12X12_UNorm.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 12×12 rectangle of unsigned normalized RGBA texel data.  
[YUV2](Experimental.Rendering.GraphicsFormat.YUV2.html)| YUV 4:2:2 Video
resource format.  
[RGBA_ASTC4X4_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC4X4_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 4×4 rectangle of float RGBA texel data.  
[RGBA_ASTC5X5_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC5X5_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 5×5 rectangle of float RGBA texel data.  
[RGBA_ASTC6X6_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC6X6_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 6×6 rectangle of float RGBA texel data.  
[RGBA_ASTC8X8_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC8X8_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes an 8×8 rectangle of float RGBA texel data.  
[RGBA_ASTC10X10_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC10X10_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 10×10 rectangle of float RGBA texel data.  
[RGBA_ASTC12X12_UFloat](Experimental.Rendering.GraphicsFormat.RGBA_ASTC12X12_UFloat.html)|
A four-component, ASTC compressed format where each 128-bit compressed texel
block encodes a 12×12 rectangle of float RGBA texel data.  
[D16_UNorm_S8_UInt](Experimental.Rendering.GraphicsFormat.D16_UNorm_S8_UInt.html)|
A two-component, 24-bit format that has 16 unsigned normalized bits in the
depth component and 8 unsigned integer bits in the stencil component. Most
platforms do not support this format.  
  
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

