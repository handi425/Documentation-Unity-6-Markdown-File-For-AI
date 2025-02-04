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

# ComputeBuffer Constructor

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

public ComputeBuffer(int count, int stride);

## Declaration

public ComputeBuffer(int count, int stride,
[ComputeBufferType](ComputeBufferType.html) type);

## Declaration

public ComputeBuffer(int count, int stride,
[ComputeBufferType](ComputeBufferType.html) type,
[ComputeBufferMode](ComputeBufferMode.html) usage);

### Parameters

count | Number of elements in the buffer.  
---|---  
stride | Size of one element in the buffer, in bytes. Must be a multiple of 4 and less than 2048, and match the size of the buffer type in the shader. See [Compute Shaders](../Manual/class-ComputeShader.html) for cross-platform compatibility information.  
type | Type of the buffer, default is [ComputeBufferType.Default](ComputeBufferType.Default.html) (structured buffer).  
usage | Usage mode of the buffer, default is ComputeBufferModeImmutable.  
  
### Description

Create a Compute Buffer.

Use [Release](ComputeBuffer.Release.html) to release the buffer when no longer
needed.  
  
Additional resources: [SystemInfo.supportsComputeShaders](SystemInfo-
supportsComputeShaders.html), [ComputeShader](ComputeShader.html) class,
[Shader.SetGlobalBuffer](Shader.SetGlobalBuffer.html),
[Material.SetBuffer](Material.SetBuffer.html), [Compute
Shaders](../Manual/class-ComputeShader.html).

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

