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

#  [SerializedProperty](SerializedProperty.html).longValue

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

public long longValue;

### Description

Value of an integer property as a long.

Contains a valid value when [propertyType](SerializedProperty-
propertyType.html) is
[SerializedPropertyType.Integer](SerializedPropertyType.Integer.html). Most
appropriate for long properties
([SerializedPropertyNumericType.Int64](SerializedPropertyNumericType.Int64.html)),
but can be used with all integer types of 64 bits or less, although
[ulongValue](SerializedProperty-ulongValue.html) is recommended for
[SerializedPropertyNumericType.UInt64](SerializedPropertyNumericType.UInt64.html).  
  
When assigning a value to [longValue](SerializedProperty-longValue.html), the
value is clamped in the range of the property's declared type. For example, a
property that is declared as a ushort is clamped between 0 and 65,535.  
  
Additional resources: [intValue](SerializedProperty-intValue.html),
[ulongValue](SerializedProperty-ulongValue.html),
[propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.Integer](SerializedPropertyType.Integer.html).

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

