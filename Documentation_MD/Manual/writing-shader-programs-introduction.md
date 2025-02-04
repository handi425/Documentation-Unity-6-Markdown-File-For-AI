[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-programs-introduction.html)
  * [中文](/cn/current/Manual/writing-shader-programs-introduction.html)
  * [日本語](/ja/current/Manual/writing-shader-programs-introduction.html)
  * [한국어](/kr/current/Manual/writing-shader-programs-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-programs-introduction.html)
  * [中文](/cn/current/Manual/writing-shader-programs-introduction.html)
  * [日本語](/ja/current/Manual/writing-shader-programs-introduction.html)
  * [한국어](/kr/current/Manual/writing-shader-programs-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * Shader program fundamentals

[](writing-shader-writing-shader-programs-hlsl.html)

Writing HLSL shader programs

[](writing-shader-add-shader-program.html)

Add an HLSL shader program

# Shader program fundamentals

In Unity, you usually write **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs in HLSL. To add HLSL code to
your [shader asset](SL-Shader.html), you put the code inside a **shader code
block**.

**Note:** Unity also supports writing shader programs in other languages,
although this is not generally needed or recommended. For more information,
see [Writing shaders](shader-writing.html).

This section of the manual includes information on using HLSL in a Unity-
specific way. For general information on writing HLSL, see [Microsoft’s HLSL
documentation](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-
graphics-hlsl).

**Note:** Unity originally used the
[Cg](https://en.wikipedia.org/wiki/Cg_%28programming_language%29) language,
hence the name of some of Unity’s keywords (`CGPROGRAM`) and file extensions
(`.cginc`). Unity no longer uses Cg, but these names are still in use.

## HLSL syntax

HLSL has two syntaxes: a legacy DirectX 9-style syntax, and a more modern
DirectX 10+ style syntax. The difference is mostly in how texture sampling
functions work:

  * The legacy syntax uses sampler2D, tex2D() and similar functions. This syntax works on all platforms.
  * The DX10+ syntax uses Texture2D, SamplerState and .Sample() functions. Some forms of this syntax do not work on OpenGL platforms, because textures and samplers are not different objects in OpenGL.

Unity provides shader libraries that contain preprocessor macros to help you
manage these differences. For more information, see [Built-in shader
macros](use-built-in-shader-methods-birp.html).

## Vertex and fragment shaders

The **Vertex Shader** A program that runs on each vertex of a 3D model when
the model is being rendered. [More info](writing-shader-writing-shader-
programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader) is a program that runs on each
vertex of the 3D model. Quite often it does not do anything particularly
interesting. Here we just transform vertex position from object space into so
called “clip space”, which is what’s used by the GPU to rasterize the object
on screen. We also pass the input texture coordinate unmodified - we’ll need
it to sample the texture in the fragment shader.

The **Fragment Shader** is a program that runs on each and every **pixel** The
smallest unit in a computer image. Pixel size depends on your screen
resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) that object occupies on-screen, and is
usually used to calculate and output the color of each pixel. Usually there
are millions of pixels on the screen, and the fragment shaders are executed
for all of them! Optimizing fragment shaders is quite an important part of
overall game performance work.

Some variable or function definitions are followed by a **Semantic Signifier**
\- for example **: POSITION** or **: SV_Target**. These semantics signifiers
communicate the “meaning” of these variables to the GPU. See the [shader
semantics](SL-VertexProgramInputs.html) page for details.

[](writing-shader-writing-shader-programs-hlsl.html)

Writing HLSL shader programs

[](writing-shader-add-shader-program.html)

Add an HLSL shader program

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

