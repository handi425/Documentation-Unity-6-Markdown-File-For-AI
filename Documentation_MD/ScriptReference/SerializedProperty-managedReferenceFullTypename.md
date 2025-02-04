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

#  [SerializedProperty](SerializedProperty.html).managedReferenceFullTypename

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

public string managedReferenceFullTypename;

### Description

String corresponding to the value of the managed reference object (dynamic)
full type string.

Contains a valid value when [propertyType](SerializedProperty-
propertyType.html) is
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html).
This property is Read Only (you cannot write to it).  
  
  
  
The full type name string returned has the following format: "[assembly-name]
[namespace.][parent-class-names][classname]" where:  
\- `[assembly-name]` is the name of the assembly that contains the target type  
\- `[namespace.]` is an optional (if empty) namespace followed by a '.'  
\- `[parent-class-names]` is a '/' separated list of optional parent class
names (in the case of nested class definitions)  
\- `[classname]` is the actual dynamic type name of the managed object class.  
  
  
  
'null' references return an empty type string.  
  
Additional resources: [propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html).

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

