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

#  [PropertyContainer](Unity.Properties.PropertyContainer.html).TryAccept

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

public static bool
TryAccept([Unity.Properties.IPropertyBagVisitor](Unity.Properties.IPropertyBagVisitor.html)
visitor, ref TContainer container,
[Unity.Properties.VisitParameters](Unity.Properties.VisitParameters.html)
parameters);

### Parameters

visitor | The visitor.  
---|---  
container | The container to visit.  
parameters | The visit parameters to use.  
  
### Returns

**bool** `true` if the visitation succeeded; `false` otherwise.

### Description

Tries to visit the specified by ref using the specified .

* * *

## Declaration

public static bool
TryAccept([Unity.Properties.IPropertyBagVisitor](Unity.Properties.IPropertyBagVisitor.html)
visitor, ref TContainer container, out
[Unity.Properties.VisitReturnCode](Unity.Properties.VisitReturnCode.html)
returnCode,
[Unity.Properties.VisitParameters](Unity.Properties.VisitParameters.html)
parameters);

### Parameters

visitor | The visitor.  
---|---  
container | The container to visit.  
parameters | The visit parameters to use.  
returnCode | When this method returns, contains the return code.  
  
### Returns

**bool** `true` if the visitation succeeded; `false` otherwise.

### Description

Tries to visit the specified by ref using the specified .

* * *

## Declaration

public static bool
TryAccept([Unity.Properties.IPropertyVisitor](Unity.Properties.IPropertyVisitor.html)
visitor, ref TContainer container, ref
[Unity.Properties.PropertyPath](Unity.Properties.PropertyPath.html) path, out
[Unity.Properties.VisitReturnCode](Unity.Properties.VisitReturnCode.html)
returnCode,
[Unity.Properties.VisitParameters](Unity.Properties.VisitParameters.html)
parameters);

### Parameters

visitor | The visitor.  
---|---  
container | The container to visit.  
path | The property path to visit.  
returnCode | When this method returns, contains the return code.  
parameters | The visit parameters to use.  
  
### Description

Visit the specified using the specified at the given
[PropertyPath](Unity.Properties.PropertyPath.html).

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

