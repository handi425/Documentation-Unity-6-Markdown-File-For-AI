[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-error.html)
  * [中文](/cn/current/Manual/shader-error.html)
  * [日本語](/ja/current/Manual/shader-error.html)
  * [한국어](/kr/current/Manual/shader-error.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-error.html)
  * [中文](/cn/current/Manual/shader-error.html)
  * [日本語](/ja/current/Manual/shader-error.html)
  * [한국어](/kr/current/Manual/shader-error.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * Error and loading shaders

[](shader-troubleshooting.html)

Troubleshooting shaders

[](shader-reduce-stalling.html)

Fixing hitches or stalls

# Error and loading shaders

Sometimes, Unity can’t render objects with regular **shaders** A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). When this happens, Unity renders the
objects with special shaders:

  * The default error shader
  * The loading shader
  * The Streaming Virtual Texturing error material

The special shader that Unity uses depends on the reason that Unity can’t use
the original shader.

## The default error shader

Unity renders an object with the default error shader when there’s a problem
with that object’s material or shader; for example, if no material is
assigned, if the shader doesn’t compile, or if the shader isn’t supported.

Unity uses the default error shader in the Unity Editor, and in builds.

The default error shader is magenta (bright pink).

![The magenta error shader.](../uploads/Main/shader-error.png) The magenta
error shader.

When you use the
[BatchRendererGroup](../ScriptReference/Rendering.BatchRendererGroup.html)
API, Unity doesn’t display the default error shader. Use
[BatchRendererGroup.SetErrorMaterial](../ScriptReference/Rendering.BatchRendererGroup.SetErrorMaterial.html)
to set a material to use instead.

If your project uses the Universal Rendering Pipeline (URP), Unity might
render an object using the default error shader if the object uses a shader
from the Built-In **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). Refer to [Converting your
shaders](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@17.0/manual/upgrading-your-shaders.html) for more
information.

## The loading shader

Unity renders an object with the loading shader to indicate that Unity is
compiling the [shader variant](shader-variants.html)A verion of a shader
program that Unity generates according to a specific combination of shader
keywords and their status. A Shader object can contain multiple shader
variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant) needed to display that object.

Unity shows the loading shader in the Unity Editor when [asynchronous shader
compilation](AsynchronousShaderCompilation.html) is enabled, or in a
**development build** A development build includes debug symbols and enables
the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-
target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild) when [Shader Live Link
support](../ScriptReference/BuildOptions.ShaderLivelinkSupport.html) is
enabled.

The loading shader is cyan (bright blue).

![The cyan loading shader.](../uploads/Main/shader-loading.png) The cyan
loading shader.

When you use the
[BatchRendererGroup](../ScriptReference/Rendering.BatchRendererGroup.html)
API, Unity doesn’t display the loading shader. Use
[BatchRendererGroup.SetLoadingMaterial](../ScriptReference/Rendering.BatchRendererGroup.SetLoadingMaterial.html)
to set a material to use instead.

## The Virtual Texturing error material

If your project uses [Streaming Virtual Texturing ](svt-streaming-virtual-
texturing.html) (SVT), Unity uses a special material to indicate problems in
your SVT setup. For more information, see [Virtual Texturing error
material](svt-error-material.html).

[](shader-troubleshooting.html)

Troubleshooting shaders

[](shader-reduce-stalling.html)

Fixing hitches or stalls

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

