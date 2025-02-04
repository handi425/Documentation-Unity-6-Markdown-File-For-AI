[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CameraOutput-troubleshoot.html)
  * [中文](/cn/current/Manual/CameraOutput-troubleshoot.html)
  * [日本語](/ja/current/Manual/CameraOutput-troubleshoot.html)
  * [한국어](/kr/current/Manual/CameraOutput-troubleshoot.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CameraOutput-troubleshoot.html)
  * [中文](/cn/current/Manual/CameraOutput-troubleshoot.html)
  * [日本語](/ja/current/Manual/CameraOutput-troubleshoot.html)
  * [한국어](/kr/current/Manual/CameraOutput-troubleshoot.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Camera output](CameraOutput.html)
  * Troubleshooting camera output

[](CameraOutput-shader.html)

Sample output textures in a shader

[](urp/urp-cameras-landing.html)

Cameras in URP

# Troubleshooting camera output

The **Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window indicates when a camera is
rendering a depth or a depth+normals texture.

The way that depth textures are requested from the Camera
([Camera.depthTextureMode](../ScriptReference/Camera-depthTextureMode.html))
might mean that after you disable an effect that needed them, the Camera might
still continue rendering them. If there are multiple effects present on a
Camera, where each of them needs the depth texture, there’s no good way to
automatically disable depth texture rendering if you disable the individual
effects.

When implementing complex **Shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) or Image Effects, keep [Rendering
Differences Between Platforms](SL-PlatformDifferences.html) in mind. In
particular, using depth texture in an Image Effect often needs special
handling on Direct3D + Anti-Aliasing.

In some cases, the depth texture might come directly from the native Z buffer.
If you see artifacts in your depth texture, make sure that the shaders that
use it **do not** write into the Z buffer (use [ZWrite Off](SL-ZWrite.html)).

When the DepthNormals texture is rendered in a separate pass, this is done
through [Shader Replacement](SL-ShaderReplacement.html). Hence it is important
to have correct “**RenderType** ” tag in your shaders.

## Additional resources

  * [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](CameraOutput-shader.html)

Sample output textures in a shader

[](urp/urp-cameras-landing.html)

Cameras in URP

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

