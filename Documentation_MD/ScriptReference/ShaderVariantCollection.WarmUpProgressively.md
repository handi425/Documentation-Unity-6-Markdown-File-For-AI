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

#  [ShaderVariantCollection](ShaderVariantCollection.html).WarmUpProgressively

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

public bool WarmUpProgressively(int variantCount);

### Parameters

variantCount | The maximum number of variants to warm up.  
---|---  
  
### Returns

**bool** True if all variants in this shader variant collection have been
warmed up, false otherwise.

### Description

Prewarms the given number of shader variants in this shader variant
collection.

For information on shader loading and prewarming, including a list of
different prewarming techniques, see [Shader loading](../Manual/shader-
loading.html).  
  
**Warning:** This method is fully supported on DX11 and OpenGL. On DX12,
Vulkan, and Metal, the graphics driver might still perform work if the vertex
layout or the render target setup is different from the data used to prewarm
it. This can result in wasted work and GPU memory, and leave visible stalls in
your application. [ShaderWarmup](Experimental.Rendering.ShaderWarmup.html) is
supported on all graphics APIs.  
  
Additional resources:
[ShaderWarmup](Experimental.Rendering.ShaderWarmup.html),
[Shader.WarmupAllShaders](Shader.WarmupAllShaders.html), [Shader
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

