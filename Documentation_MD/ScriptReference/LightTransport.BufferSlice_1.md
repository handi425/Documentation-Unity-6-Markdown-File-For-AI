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

# BufferSlice<T0>

struct in UnityEngine.LightTransport

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

Unity uses the BufferSlice struct to split one large buffer allocation into
one or more smaller buffers, each with explicit types.

### Properties

[Id](LightTransport.BufferSlice_1.Id.html)| Buffer ID.  
---|---  
[Offset](LightTransport.BufferSlice_1.Offset.html)| The number of elements to
offset, measured from the beginning of the buffer. The value must not exceed
the end of the buffer allocation.  
  
### Constructors

[BufferSlice_1](LightTransport.BufferSlice_1-ctor.html)| Construct a new
BufferSlice struct by defining an offset from the beginning of a buffer. The
buffer is defined by the BufferID.  
---|---  
  
### Public Methods

[SafeReinterpret](LightTransport.BufferSlice_1.SafeReinterpret.html)|
Reinterpret the slice as having a different data type (type punning),
performing checks to ensure the reinterpret is valid.  
---|---  
[UnsafeReinterpret](LightTransport.BufferSlice_1.UnsafeReinterpret.html)|
Reinterpret the slice as having a different data type (type punning), but does
not check if the reinterpret is valid.  
  
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

