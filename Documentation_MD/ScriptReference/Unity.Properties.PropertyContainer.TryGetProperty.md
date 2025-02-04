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

#  [PropertyContainer](Unity.Properties.PropertyContainer.html).TryGetProperty

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

public static bool TryGetProperty(TContainer container, ref
[Unity.Properties.PropertyPath](Unity.Properties.PropertyPath.html) path, out
[Unity.Properties.IProperty](Unity.Properties.IProperty.html) property);

### Parameters

container | The container tree to search.  
---|---  
path | The property path to resolve.  
property | When this method returns, contains the property associated with the specified path, if the property is found; otherwise, null.  
  
### Returns

**bool** `true` if the property was found at the specified path; otherwise,
`false`.

### Description

Gets an [IProperty](Unity.Properties.IProperty.html) on the specified
container for the given [PropertyPath](Unity.Properties.PropertyPath.html).

While the container data is not actually read from or written to. The
container itself is needed to resolve polymorphic fields and list elements.

* * *

## Declaration

public static bool TryGetProperty(ref TContainer container, ref
[Unity.Properties.PropertyPath](Unity.Properties.PropertyPath.html) path, out
[Unity.Properties.IProperty](Unity.Properties.IProperty.html) property, out
[Unity.Properties.VisitReturnCode](Unity.Properties.VisitReturnCode.html)
returnCode);

### Parameters

container | The container tree to search.  
---|---  
path | The property path to resolve.  
property | When this method returns, contains the property associated with the specified path, if the property is found; otherwise, null.  
returnCode | When this method returns, contains the return code.  
  
### Returns

**bool** `true` if the property was found at the specified path; otherwise,
`false`.

### Description

Gets an [IProperty](Unity.Properties.IProperty.html) on the specified
container for the given [PropertyPath](Unity.Properties.PropertyPath.html).

While the container data is not actually read from or written to. The
container itself is needed to resolve polymorphic fields and list elements.

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

