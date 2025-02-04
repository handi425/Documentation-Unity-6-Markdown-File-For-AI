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

#  [MaterialPropertyBlock](MaterialPropertyBlock.html).SetVectorArray

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

public void SetVectorArray(string name, Vector4[] values);

## Declaration

public void SetVectorArray(int nameID, Vector4[] values);

## Declaration

public void SetVectorArray(string name, List<Vector4> values);

## Declaration

public void SetVectorArray(int nameID, List<Vector4> values);

### Parameters

nameID | The name ID of the property retrieved by [Shader.PropertyToID](Shader.PropertyToID.html).  
---|---  
values | The array to set.  
name | The name of the property.  
  
### Description

Set a vector array property.

Adds a vector array property to the block. If a vector array property with the
given name already exists, the old value is replaced.  
  
The array length can't be changed once it has been added to the block. If you
subsequently try to set a longer array into the same property, the length will
be capped to the original length and the extra items you tried to assign will
be ignored. If you set a shorter array than the original length, your values
will be assigned but the original values will remain for the array elements
beyond the length of your new shorter array.  
  
Additional resources:
[SetFloatArray](MaterialPropertyBlock.SetFloatArray.html),
[SetMatrixArray](MaterialPropertyBlock.SetMatrixArray.html).

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

