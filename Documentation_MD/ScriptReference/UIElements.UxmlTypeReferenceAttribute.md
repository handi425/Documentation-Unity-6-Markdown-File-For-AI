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

# UxmlTypeReferenceAttribute

class in UnityEngine.UIElements

/

Inherits from:[PropertyAttribute](PropertyAttribute.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Provides information about the expected type when applied to a Type field or
property that has the
[UxmlAttributeAttribute](UIElements.UxmlAttributeAttribute.html) attribute.

When defining a Type field or property with the
[UxmlAttributeAttribute](UIElements.UxmlAttributeAttribute.html) in Unity, you
can use the UxmlTypeReference attribute to specify the base type that the
value should inherit from. This allows you to provide additional information
about the expected type of the value and helps Unity ensure that the correct
type is assigned to the attribute.  
  
The following example creates a custom control and restricts the attribute
type to only accept values that are derived from
[VisualElement](UIElements.VisualElement.html):

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine.UIElements;  
      
    [UxmlElement]
    public partial class TypeRestrictionExample : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute, UxmlTypeReference(typeof([VisualElement](UIElements.VisualElement.html)))]
        public Type elementType { get; set; }
    }
    

### Properties

[baseType](UIElements.UxmlTypeReferenceAttribute-baseType.html)|  The base
type that the value inherits from.  
---|---  
  
### Constructors

[UxmlTypeReferenceAttribute](UIElements.UxmlTypeReferenceAttribute-ctor.html)|
Provides information about the expected type when applied to a Type field or
property that has the UxmlAttributeAttribute attribute.  
---|---  
  
### Inherited Members

### Properties

[applyToCollection](PropertyAttribute-applyToCollection.html)| Makes attribute
affect collections instead of their items.  
---|---  
[order](PropertyAttribute-order.html)| Optional field to specify the order
that multiple DecorationDrawers should be drawn in.  
  
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

