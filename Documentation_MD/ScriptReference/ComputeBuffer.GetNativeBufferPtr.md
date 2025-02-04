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

#  [ComputeBuffer](ComputeBuffer.html).GetNativeBufferPtr

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

public IntPtr GetNativeBufferPtr();

### Returns

**IntPtr** Pointer to the underlying graphics API buffer.

### Description

Retrieve a native (underlying graphics API) pointer to the buffer.

Use this function to retrieve a pointer/handle corresponding to the compute
buffer, as it is represented in the native graphics API. This can be used to
enable compute buffer data manipulation from [native code
plugins](../Manual/native-plugin-interface.html).  
  
Note: When you use the Unity APIs to modify the buffer data, it changes the
underlying graphics API native pointer. Call GetNativeBufferPtr to get the new
native pointer.  
  
The type of data returned depends on the underlying graphics API: ID3D11Buffer
on D3D11, ID3D12Resource on D3D12, buffer "name" (as GLuint) on OpenGL/ES,
MTLBuffer on Metal. Platforms that do not support compute shaders will always
return NULL.  
  
Note that calling this function when using multi-threaded rendering will
synchronize with the rendering thread (a slow operation), so best practice is
to set up needed buffer pointers only at initialization time.  
  
Additional resources: [Native code plugins](../Manual/native-plugin-
interface.html).

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

