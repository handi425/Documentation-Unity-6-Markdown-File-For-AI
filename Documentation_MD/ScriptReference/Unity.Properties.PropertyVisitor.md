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

# PropertyVisitor

class in Unity.Properties

/

Implemented
in:[UnityEngine.PropertiesModule](UnityEngine.PropertiesModule.html)

Leave feedback

  

Implements
interfaces:[ICollectionPropertyVisitor](Unity.Properties.ICollectionPropertyVisitor.html),
[IDictionaryPropertyBagVisitor](Unity.Properties.IDictionaryPropertyBagVisitor.html),
[IDictionaryPropertyVisitor](Unity.Properties.IDictionaryPropertyVisitor.html),
[IListPropertyBagVisitor](Unity.Properties.IListPropertyBagVisitor.html),
[IListPropertyVisitor](Unity.Properties.IListPropertyVisitor.html),
[IPropertyBagVisitor](Unity.Properties.IPropertyBagVisitor.html),
[IPropertyVisitor](Unity.Properties.IPropertyVisitor.html),
[ISetPropertyVisitor](Unity.Properties.ISetPropertyVisitor.html)

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

Base class for implementing algorithms using properties. This is an abstract
class.

### Public Methods

[AddAdapter](Unity.Properties.PropertyVisitor.AddAdapter.html)|  Adds an
adapter to the visitor.  
---|---  
[RemoveAdapter](Unity.Properties.PropertyVisitor.RemoveAdapter.html)|  Removes
an adapter from the visitor.  
  
### Protected Methods

[IsExcluded](Unity.Properties.PropertyVisitor.IsExcluded.html)|  Called before
visiting each property to determine if the property should be visited.  
---|---  
[VisitCollection](Unity.Properties.PropertyVisitor.VisitCollection.html)|
Called when visiting any non-specialized collection property.  
[VisitDictionary](Unity.Properties.PropertyVisitor.VisitDictionary.html)|
Called when visiting a specialized dictionary property.  
[VisitList](Unity.Properties.PropertyVisitor.VisitList.html)|  Called when
visiting a specialized list property.  
[VisitProperty](Unity.Properties.PropertyVisitor.VisitProperty.html)|  Called
when visiting any leaf property with no specialized handling.  
[VisitSet](Unity.Properties.PropertyVisitor.VisitSet.html)|  Called when
visiting a specialized set property.  
  
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

