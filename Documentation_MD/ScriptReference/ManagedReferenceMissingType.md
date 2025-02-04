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

# ManagedReferenceMissingType

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

Represents a managed reference object that has a missing type.

ManagedReferenceMissingType describes a managed reference object that could
not be deserialized because it is missing its type.  
  
It includes the details of the type (expressed by its assembly, class and
namespace) that is expected in order to reinstantiate the object.  
  
A type can be missing if the class was renamed, moved to another assembly, or
moved inside a different namespace. A missing type may be a sign that an
entire assembly or source script is missing from the project.  
  
If the original types are not available, this info can aid in migrating data
to new types, or making a decision to clear the associated data.  
  
Additional resources:
[SerializationUtility.HasManagedReferencesWithMissingTypes](SerializationUtility.HasManagedReferencesWithMissingTypes.html),
[SerializationUtility.GetManagedReferencesWithMissingTypes](SerializationUtility.GetManagedReferencesWithMissingTypes.html),
[SerializationUtility.ClearManagedReferenceWithMissingType](SerializationUtility.ClearManagedReferenceWithMissingType.html),
[SerializeReference](SerializeReference.html)

### Properties

[assemblyName](ManagedReferenceMissingType-assemblyName.html)| Name of the
Assembly where Unity expects to find the class. (Read Only)  
---|---  
[className](ManagedReferenceMissingType-className.html)| Name of the class
that is needed to instantiate the Managed Reference. (Read Only)  
[namespaceName](ManagedReferenceMissingType-namespaceName.html)| Namespace
where Unity expects to find the class. Namespaces are optional so this might
contain an empty string. (Read Only)  
[referenceId](ManagedReferenceMissingType-referenceId.html)| The Managed
Reference ID. (Read Only)  
[serializedData](ManagedReferenceMissingType-serializedData.html)| String
summarizing the content of the serialized data of the missing object. (Read
Only)  
  
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

