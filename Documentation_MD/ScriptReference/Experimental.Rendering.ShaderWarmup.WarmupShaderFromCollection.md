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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[ShaderWarmup](Experimental.Rendering.ShaderWarmup.html).WarmupShaderFromCollection

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

## Declaration

public static void
WarmupShaderFromCollection([ShaderVariantCollection](ShaderVariantCollection.html)
collection, [Shader](Shader.html) shader,
[Experimental.Rendering.ShaderWarmupSetup](Experimental.Rendering.ShaderWarmupSetup.html)
setup);

### Description

Prewarms the shader variants for a given [Shader](Shader.html) that are in a
given [ShaderVariantCollection](ShaderVariantCollection.html), using a given
rendering configuration.

For information on shader loading and prewarming, including a list of
different prewarming techniques, see [Shader loading](../Manual/shader-
loading.html).  
  
Unity needs more information to correctly build GPU representations of the
shader variants ('pipeline state objects' or PSOs) if your application runs on
one of the following graphics APIs:

  * DirectX 12
  * Metal
  * Vulkan

If Unity has this information, it's more likely the prewarmed variants match
what the GPU needs when it renders your Scene.  
  
To provide Unity with more information, you can do the following:

  * Use the `setup` parameter to specify the vertex data layout you use with the shader.
  * Before you call `WarmupShader`, set the render state so it's as close as possible to the state you use with the shader. For example, set the [format of the render target](RenderTextureFormat.html), or use [render state commands](../Manual/shader-shaderlab-commands.html) to set states such as blend mode.

Unity also asynchronously prewarms shader variants using multiple background
threads, if your application runs on a platform that supports it. Unity uses
as many threads as it can. In your built application, you can use the `-max-
async-pso-job-count` [command line
argument](../Manual/PlayerCommandLineArguments.html) to set the number of
threads Unity uses.  
  
Additional resources:
[ShaderWarmup.WarmupShader](Experimental.Rendering.ShaderWarmup.WarmupShader.html),
[Shader.WarmupAllShaders](Shader.WarmupAllShaders.html),
[ShaderVariantCollection.WarmUp](ShaderVariantCollection.WarmUp.html), [Shader
loading](../Manual/shader-loading.html)

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

