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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetRandomWriteTarget

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

public void SetRandomWriteTarget(int index,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) rt);

## Declaration

public void SetRandomWriteTarget(int index,
[ComputeBuffer](ComputeBuffer.html) buffer, bool preserveCounterValue);

## Declaration

public void SetRandomWriteTarget(int index,
[ComputeBuffer](ComputeBuffer.html) buffer);

## Declaration

public void SetRandomWriteTarget(int index,
[GraphicsBuffer](GraphicsBuffer.html) buffer, bool preserveCounterValue);

## Declaration

public void SetRandomWriteTarget(int index,
[GraphicsBuffer](GraphicsBuffer.html) buffer);

### Parameters

index | Index of the random write target in the shader.  
---|---  
buffer | Buffer to set as the write target.  
preserveCounterValue | Whether to leave the append/consume counter value unchanged.  
rt | RenderTargetIdentifier to set as the write target.  
  
### Description

Set random write target for [Shader Model 4.5](../Manual/SL-
ShaderCompileTargets.html) level pixel shaders.

This is the CommandBuffer equivalent of
[Graphics.SetRandomWriteTarget](Graphics.SetRandomWriteTarget.html). The same
limitations and exceptions apply to this call as to
[Graphics.SetRandomWriteTarget](Graphics.SetRandomWriteTarget.html).

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

