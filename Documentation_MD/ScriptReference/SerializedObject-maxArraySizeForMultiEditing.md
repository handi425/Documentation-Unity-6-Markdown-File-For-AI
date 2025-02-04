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

#  [SerializedObject](SerializedObject.html).maxArraySizeForMultiEditing

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

public int maxArraySizeForMultiEditing;

### Description

Defines the maximum size beyond which arrays cannot be edited when multiple
objects are selected.

This value controls the maximum array size that you can edit during multiple-
object-editing in the Inspector.  
  
When you select two or more GameObjects and the minimum array size for a
property is larger than this value, the Inspector shows an empty array and
[SerializedProperty.arraySize](SerializedProperty-arraySize.html) returns 0.
In that case, [SerializedProperty.minArraySize](SerializedProperty-
minArraySize.html) exposes the actual minimum size.  
  
As a compromise between performance and utility, the default array size is 64.  
  
If your serialized object typically has arrays larger than this, you can set
this value to a higher number to allow multi-editing on those arrays. Please
be aware that setting too high a value might affect Inspector performance when
editing large arrays or a large number of objects.

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

