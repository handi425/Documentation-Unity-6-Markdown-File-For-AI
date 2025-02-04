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

#  [ComputeShader](ComputeShader.html).SetMatrix

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public void SetMatrix(string name, [Matrix4x4](Matrix4x4.html) val);

## Declaration

public void SetMatrix(int nameID, [Matrix4x4](Matrix4x4.html) val);

### Parameters

name | Variable name in shader code.  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
val | Value to set.  
  
### Description

Set a Matrix parameter.

Constant buffers are shared between all kernels in a single compute shader
asset. Therefore this function affects all kernels in this ComputeShader.  
  
Additional resources: [SetFloat](ComputeShader.SetFloat.html),
[SetFloats](ComputeShader.SetFloats.html),
[SetInt](ComputeShader.SetInt.html), [SetInts](ComputeShader.SetInts.html),
[SetBool](ComputeShader.SetBool.html),
[SetBuffer](ComputeShader.SetBuffer.html),
[SetMatrixArray](ComputeShader.SetMatrixArray.html),
[SetTexture](ComputeShader.SetTexture.html),
[SetVector](ComputeShader.SetVector.html),
[SetVectorArray](ComputeShader.SetVectorArray.html).

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

