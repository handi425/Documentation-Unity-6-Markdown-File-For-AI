[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-CameraDepthTexture.html)
  * [中文](/cn/current/Manual/SL-CameraDepthTexture.html)
  * [日本語](/ja/current/Manual/SL-CameraDepthTexture.html)
  * [한국어](/kr/current/Manual/SL-CameraDepthTexture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-CameraDepthTexture.html)
  * [中文](/cn/current/Manual/SL-CameraDepthTexture.html)
  * [日本語](/ja/current/Manual/SL-CameraDepthTexture.html)
  * [한국어](/kr/current/Manual/SL-CameraDepthTexture.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Camera output](CameraOutput.html)
  * Output a depth texture from a camera

[](CameraOutput-introduction.html)

Introduction to camera output

[](SL-CameraDepthTexture-motionvectors.html)

Output a motion vector texture from a camera

# Output a depth texture from a camera

Use `DepthTextureMode` to output a depth texture or a depth-normals texture
from a **camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

## DepthTextureMode.Depth texture

This builds a screen-sized depth texture.

Depth texture is rendered using the same **shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) passes as used for shadow caster
rendering (`ShadowCaster` pass type). So by extension, if a shader does not
support shadow casting (i.e. there’s no shadow caster pass in the shader or
any of the fallbacks), then objects using that shader will not show up in the
depth texture.

  * Make your shader [fallback](SL-Fallback.html) to some other shader that has a shadow casting pass, or
  * If you’re using [surface shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader), adding an `addshadow`
directive will make them generate a shadow pass too.

Note that only “opaque” objects (that which have their materials and shaders
setup to use [render queue](SL-SubShaderTags.html) <= 2500) are rendered into
the depth texture.

## DepthTextureMode.DepthNormals texture

This builds a screen-sized 32 bit (8 bit/channel) texture, where view space
normals are encoded into R&G channels, and depth is encoded in B&A channels.
Normals are encoded using Stereographic projection, and depth is 16 bit value
packed into two 8 bit channels.

[`UnityCG.cginc` include file](SL-BuiltinIncludes.html) has a helper function
`DecodeDepthNormal` to decode depth and normal from the encoded **pixel** The
smallest unit in a computer image. Pixel size depends on your screen
resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) value. Returned depth is in 0..1 range.

For examples on how to use the depth and normals texture, please refer to
[Replacing shaders at runtime](SL-ShaderReplacement.html) or **Ambient
Occlusion** A method to approximate how much ambient light (light not coming
from a specific direction) can hit a point on a surface.  
See in [Glossary](Glossary.html#Ambientocclusion) in [Post-processing and
full-screen effects](PostProcessingOverview.html).

## Additional resources

  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](CameraOutput-introduction.html)

Introduction to camera output

[](SL-CameraDepthTexture-motionvectors.html)

Output a motion vector texture from a camera

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

