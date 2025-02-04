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

# BlendOp

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

Blend operation.

The blend operation that is used to combine the pixel shader output with the
render target. This can be passed through Material.SetInt() to change the
blend operation during runtime.  
  
Note that the logical operations are only supported in Gamma (non-sRGB)
colorspace, on DX11.1 hardware running on DirectX 11.1 runtime.  
  
Advanced OpenGL blend operations are supported only on hardware supporting
either GL_KHR_blend_equation_advanced or GL_NV_blend_equation_advanced and may
require use of [GL.RenderTargetBarrier](GL.RenderTargetBarrier.html). In
addition, the shaders that are used with the advanced blend operations must
have a UNITY_REQUIRE_ADVANDED_BLEND(mode) declaration in the shader code where
mode is one of the blend operations or "all_equations" for supporting all
advanced blend operations (see the KHR_blend_equation_advanced spec for other
values).

### Properties

[Add](Rendering.BlendOp.Add.html)| Add (s + d).  
---|---  
[Subtract](Rendering.BlendOp.Subtract.html)| Subtract.  
[ReverseSubtract](Rendering.BlendOp.ReverseSubtract.html)| Reverse subtract.  
[Min](Rendering.BlendOp.Min.html)| Min.  
[Max](Rendering.BlendOp.Max.html)| Max.  
[LogicalClear](Rendering.BlendOp.LogicalClear.html)| Logical Clear (0).  
[LogicalSet](Rendering.BlendOp.LogicalSet.html)| Logical SET (1) (D3D11.1
only).  
[LogicalCopy](Rendering.BlendOp.LogicalCopy.html)| Logical Copy (s) (D3D11.1
only).  
[LogicalCopyInverted](Rendering.BlendOp.LogicalCopyInverted.html)| Logical
inverted Copy (!s) (D3D11.1 only).  
[LogicalNoop](Rendering.BlendOp.LogicalNoop.html)| Logical No-op (d) (D3D11.1
only).  
[LogicalInvert](Rendering.BlendOp.LogicalInvert.html)| Logical Inverse (!d)
(D3D11.1 only).  
[LogicalAnd](Rendering.BlendOp.LogicalAnd.html)| Logical AND (s & d) (D3D11.1
only).  
[LogicalNand](Rendering.BlendOp.LogicalNand.html)| Logical NAND !(s & d).
D3D11.1 only.  
[LogicalOr](Rendering.BlendOp.LogicalOr.html)| Logical OR (s | d) (D3D11.1 only).  
[LogicalNor](Rendering.BlendOp.LogicalNor.html)| Logical NOR !(s | d) (D3D11.1 only).  
[LogicalXor](Rendering.BlendOp.LogicalXor.html)| Logical XOR (s XOR d)
(D3D11.1 only).  
[LogicalEquivalence](Rendering.BlendOp.LogicalEquivalence.html)| Logical
Equivalence !(s XOR d) (D3D11.1 only).  
[LogicalAndReverse](Rendering.BlendOp.LogicalAndReverse.html)| Logical reverse
AND (s & !d) (D3D11.1 only).  
[LogicalAndInverted](Rendering.BlendOp.LogicalAndInverted.html)| Logical
inverted AND (!s & d) (D3D11.1 only).  
[LogicalOrReverse](Rendering.BlendOp.LogicalOrReverse.html)| Logical reverse OR (s | !d) (D3D11.1 only).  
[LogicalOrInverted](Rendering.BlendOp.LogicalOrInverted.html)| Logical inverted OR (!s | d) (D3D11.1 only).  
[Multiply](Rendering.BlendOp.Multiply.html)| Multiply (Advanced OpenGL
blending).  
[Screen](Rendering.BlendOp.Screen.html)| Screen (Advanced OpenGL blending).  
[Overlay](Rendering.BlendOp.Overlay.html)| Overlay (Advanced OpenGL blending).  
[Darken](Rendering.BlendOp.Darken.html)| Darken (Advanced OpenGL blending).  
[Lighten](Rendering.BlendOp.Lighten.html)| Lighten (Advanced OpenGL blending).  
[ColorDodge](Rendering.BlendOp.ColorDodge.html)| Color dodge (Advanced OpenGL
blending).  
[ColorBurn](Rendering.BlendOp.ColorBurn.html)| Color burn (Advanced OpenGL
blending).  
[HardLight](Rendering.BlendOp.HardLight.html)| Hard light (Advanced OpenGL
blending).  
[SoftLight](Rendering.BlendOp.SoftLight.html)| Soft light (Advanced OpenGL
blending).  
[Difference](Rendering.BlendOp.Difference.html)| Difference (Advanced OpenGL
blending).  
[Exclusion](Rendering.BlendOp.Exclusion.html)| Exclusion (Advanced OpenGL
blending).  
[HSLHue](Rendering.BlendOp.HSLHue.html)| HSL Hue (Advanced OpenGL blending).  
[HSLSaturation](Rendering.BlendOp.HSLSaturation.html)| HSL saturation
(Advanced OpenGL blending).  
[HSLColor](Rendering.BlendOp.HSLColor.html)| HSL color (Advanced OpenGL
blending).  
[HSLLuminosity](Rendering.BlendOp.HSLLuminosity.html)| HSL luminosity
(Advanced OpenGL blending).  
  
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

