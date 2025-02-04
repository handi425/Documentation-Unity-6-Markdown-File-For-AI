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

# UxmlObjectReferenceAttribute Constructor

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

public UxmlObjectReferenceAttribute();

### Description

Declares that a field or property is associated with nested UXML objects.

* * *

## Declaration

public UxmlObjectReferenceAttribute(string uxmlName);

### Parameters

uxmlName | The name of the nested UXML element that the UXML Objects are serialized to. **Note** : This field can not be null or empty.  
---|---  
  
### Description

Declares that a field or property is associated with nested UXML objects.

* * *

## Declaration

public UxmlObjectReferenceAttribute(string uxmlName, params Type[]
acceptedTypes);

### Parameters

uxmlName | The name of the nested UXML element that the UXML Objects are serialized to. **Note** : A null or empty value will result in the objects being serialized into the root.  
---|---  
acceptedTypes | In UI Builder, when adding a UXML Object to a field that has multiple derived types, a dropdown list appears with a selection of available types that can be added to the field. By default, this list comprises all types that inherit from the UXML object type. You can use a parameter to specify a list of accepted types to be displayed, rather than showing all available types.  
  
### Description

Declares that a field or property is associated with nested UXML objects.

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

