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

#
[SerializationUtility](SerializationUtility.html).HasManagedReferencesWithMissingTypes

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

public static bool HasManagedReferencesWithMissingTypes([Object](Object.html)
obj);

### Description

This API returns true if one or more managed references is missing its type.

Managed references are objects that are referenced from a
[MonoBehaviour](MonoBehaviour.html), [ScriptableObject](ScriptableObject.html)
or other "host" object using the [SerializeReference](SerializeReference.html)
attribute. When managed references are serialized, their type information is
persisted by recording the namespace, class name and assembly name.  
  
When an asset is deserialized, the recorded type information is used to
reinstantiate the object. If the recorded type is missing during this process,
then the fields on the C# object referencing that object remain null. However
the persisted state of the object is retained and included when the asset is
resaved.  
  
If the missing types become available at a later time, for example by adding a
missing assembly or source file to the project, then the state of the Managed
Reference object can be recovered.  
  
Additional resources:
[GetManagedReferencesWithMissingTypes](SerializationUtility.GetManagedReferencesWithMissingTypes.html),
[ClearAllManagedReferencesWithMissingTypes](SerializationUtility.ClearAllManagedReferencesWithMissingTypes.html),
[SerializeReference](SerializeReference.html).

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

