[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Texture2DArray-render-target.html)
  * [中文](/cn/current/Manual/class-Texture2DArray-render-target.html)
  * [日本語](/ja/current/Manual/class-Texture2DArray-render-target.html)
  * [한국어](/kr/current/Manual/class-Texture2DArray-render-target.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Texture2DArray-render-target.html)
  * [中文](/cn/current/Manual/class-Texture2DArray-render-target.html)
  * [日本語](/ja/current/Manual/class-Texture2DArray-render-target.html)
  * [한국어](/kr/current/Manual/class-Texture2DArray-render-target.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [2D texture arrays](class-Texture2DArray.html)
  * Render to a 2D texture array

[](class-Texture2DArray-create.html)

Create a 2D texture array in a script

[](class-Texture2DArray-use-in-shader.html)

Sample a 2D texture array in a shader

# Render to a 2D texture array

To render to a 2D texture array, create a [render texture](render-texture-
landing.html)A special type of Texture that is created and updated at runtime.
To use them, first create a new Render Texture and designate one of your
Cameras to render into it. Then you can use the Render Texture in a Material
just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) and set the **Dimension**
property to **2D Array**.

If you use the
[`Graphics.SetRenderTarget`](../ScriptReference/Graphics.SetRenderTarget.html)
API, set the `depthSlice` parameter to the slice you want to render to.

If the platform supports geometry shaders, use a geometry **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) to render to individual slices, or set
`depthSlice` to `-1` to render to all the slices.

[](class-Texture2DArray-create.html)

Create a 2D texture array in a script

[](class-Texture2DArray-use-in-shader.html)

Sample a 2D texture array in a shader

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

