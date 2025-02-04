[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/material-properties-texture-properties.html)
  * [中文](/cn/current/Manual/material-properties-texture-properties.html)
  * [日本語](/ja/current/Manual/material-properties-texture-properties.html)
  * [한국어](/kr/current/Manual/material-properties-texture-properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/material-properties-texture-properties.html)
  * [中文](/cn/current/Manual/material-properties-texture-properties.html)
  * [日本語](/ja/current/Manual/material-properties-texture-properties.html)
  * [한국어](/kr/current/Manual/material-properties-texture-properties.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * Texture properties

[](SL-PropertiesInPrograms.html)

Add material properties

[](writing-shader-use-material-properties-code.html)

Access material properties in a script

# Texture properties

For each texture that is setup as a **shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader)/material property, Unity also sets up
some extra information in additional vector properties.

## Texture tiling & offset

[Materials](class-Material.html)An asset that defines how a surface should be
rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) often have Tiling and Offset fields
for their texture properties. This information is passed into shaders in a
float4 _{TextureName}_`_ST` property:

  * `x` contains X tiling value
  * `y` contains Y tiling value
  * `z` contains X offset value
  * `w` contains Y offset value

For example, if a shader contains texture named `_MainTex`, the tiling
information will be in a `_MainTex_ST` vector.

## Texture size

_{TextureName}_`_TexelSize` \- a float4 property contains texture size
information:

  * `x` contains 1.0/width
  * `y` contains 1.0/height
  * `z` contains width
  * `w` contains height

## Texture HDR parameters

_{TextureName}_`_HDR` \- a float4 property with information on how to decode a
potentially **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) (e.g. RGBM-encoded) texture depending on
the [color space](color-spaces-landing.html) used. See `DecodeHDR` function in
[UnityCG.cginc](SL-BuiltinIncludes.html) shader include file.

[](SL-PropertiesInPrograms.html)

Add material properties

[](writing-shader-use-material-properties-code.html)

Access material properties in a script

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

