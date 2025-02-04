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

# ShaderCompilerPlatform

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

Shader compiler used to generate player data shader variants.

In Unity, [shader programs](../Manual/SL-ShaderPrograms.html) are written in a
variant of [HLSL](../Manual/SL-ShadingLanguage.html) language.  
  
Each [platform](../Manual/PlatformSpecific.html) supports one or multiple
graphics APIs. For example, Vulkan and Direct3D 12 are both supported in
Windows. When building a standalone player, for each supported graphics API,
Unity runs a corresponding shader compiler which generates the shader variants
and cross-compiles the shader snippet into the shading language natively
supported by the graphics API.  
  
Additional resources:
[IPreprocessShaders.OnProcessShader](Build.IPreprocessShaders.OnProcessShader.html),
[Shader language](../Manual/SL-ShadingLanguage.html).

### Properties

[None](Rendering.ShaderCompilerPlatform.None.html)| Provide a reasonable value
for non initialized variables.  
---|---  
[D3D](Rendering.ShaderCompilerPlatform.D3D.html)| Compiler used with Direct3D
11 and Direct3D 12 graphics API on Windows platforms.  
[GLES3x](Rendering.ShaderCompilerPlatform.GLES3x.html)| Compiler used with
OpenGL ES 3.x and WebGL 2.0 graphics APIs on Android, iOS, Windows and WebGL
platforms.  
[Metal](Rendering.ShaderCompilerPlatform.Metal.html)| Compiler used with Metal
graphics API on macOS, iOS and tvOS platforms.  
[OpenGLCore](Rendering.ShaderCompilerPlatform.OpenGLCore.html)| Compiler used
with OpenGL core graphics API on macOS, Linux and Windows platforms.  
[Vulkan](Rendering.ShaderCompilerPlatform.Vulkan.html)| Compiler used with
Vulkan graphics API on Android, Linux and Windows platforms.  
[WebGPU](Rendering.ShaderCompilerPlatform.WebGPU.html)| Compiler used with
WebGPU graphics API.  
  
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

