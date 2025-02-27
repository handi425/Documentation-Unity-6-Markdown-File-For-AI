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

#  [ComputeBufferType](ComputeBufferType.html).Default

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

Default [ComputeBuffer](ComputeBuffer.html) type (structured buffer).

In HLSL shaders, this maps to `StructuredBuffer<T>` or
`RWStructuredBuffer<T>`.  
  
When you construct a ComputeBuffer of this type, the value of `stride` must
match the stride of the corresponding `StructuredBuffer` struct type in your
HLSL code.  
  
The value of `stride` must also be a multiple of 4, and less than 2048.  
  
To meet requirements on some platforms and avoid performance issues, `stride`
should be a multiple of 16. Use float4 and float4x4 variables to create a
multiple of 16, and put smaller variables inside them. Avoid the use of
'padding' variables to create a multiple of 16, for example using a float3
variable to pad a struct containing a single float, because some data types
may be different sizes on different platforms.  
  
If you use a mix of variable sizes, the data layout of a shader's structured
buffer may be different depending on the graphics API. This means
[ComputeShader.SetBuffer](ComputeShader.SetBuffer.html) or
[Material.SetBuffer](Material.SetBuffer.html) might overwrite data or set
variables to the wrong values. See [Writing shaders for different graphics
APIs](../Manual/SL-PlatformDifferences.html) for more information.  
  
See Microsoft's HLSL documentation on
[StructuredBuffer](https://msdn.microsoft.com/en-
us/library/windows/desktop/ff471514.aspx) and
[RWStructuredBuffer](https://msdn.microsoft.com/en-
us/library/windows/desktop/ff471494.aspx).  
  
Additional resources: [ComputeBuffer](ComputeBuffer.html),
[ComputeShader](ComputeShader.html),
[Material.SetBuffer](Material.SetBuffer.html).

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

