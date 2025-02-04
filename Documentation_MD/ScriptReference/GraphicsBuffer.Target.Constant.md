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

#  [GraphicsBuffer.Target](GraphicsBuffer.Target.html).Constant

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

GraphicsBuffer can be used as a constant buffer (uniform buffer).

If you use this target, you can use the [GraphicsBuffer](GraphicsBuffer.html)
as a parameter to
[ComputeShader.SetConstantBuffer](ComputeShader.SetConstantBuffer.html) and
[Material.SetConstantBuffer](Material.SetConstantBuffer.html).  
  
If you also need the buffer to be bound as a structured buffer, you must add
the [GraphicsBuffer.Target.Structured](GraphicsBuffer.Target.Structured.html)
flag. Some renderers (such as DX11) do not support binding buffers as both
constant and structured buffers.  
  
The data layout of a shader's constant buffer may be different depending on
the graphics API. This means
[ComputeShader.SetConstantBuffer](ComputeShader.SetConstantBuffer.html) or
[Material.SetConstantBuffer](Material.SetConstantBuffer.html) might overwrite
data or set variables to the wrong values. See [Writing shaders for different
graphics APIs](../Manual/SL-PlatformDifferences.html) for more information.

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

