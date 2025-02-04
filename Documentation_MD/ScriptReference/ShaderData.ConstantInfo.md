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

# ConstantInfo

struct in UnityEditor

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

Provides information about a shader constant (uniform) value.

### Properties

[ArraySize](ShaderData.ConstantInfo.ArraySize.html)| The number of elements in
this constant (Read Only). If this value is greater than 1, the constant is an
array.  
---|---  
[Columns](ShaderData.ConstantInfo.Columns.html)| If the constant is a matrix
or vector type, this stores the number of columns. Otherwise, the value is 0.
(Read Only)  
[ConstantType](ShaderData.ConstantInfo.ConstantType.html)| This constant's
type (Read Only).  
[DataType](ShaderData.ConstantInfo.DataType.html)| The element data type of
this constant (Read Only).  
[Index](ShaderData.ConstantInfo.Index.html)| The index of this constant in its
buffer (Read Only). Typically, this is the byte offset from the start of the
cbuffer, but depending on the platform, it may indicate another type of index.  
[Name](ShaderData.ConstantInfo.Name.html)| The name of this constant (Read
Only).  
[Rows](ShaderData.ConstantInfo.Rows.html)| If the constant is a matrix type,
this stores the number of rows. If the constant is a vector type, this value
will be 1. Otherwise, the value is 0. (Read Only)  
[StructFields](ShaderData.ConstantInfo.StructFields.html)| If the constant is
a struct, this stores the fields of that struct. Otherwise, the value is null.
(Read Only)  
[StructSize](ShaderData.ConstantInfo.StructSize.html)| If the constant is a
struct, this stores the size (in bytes) of the struct. Otherwise, the value is
0. (Read Only)  
  
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

