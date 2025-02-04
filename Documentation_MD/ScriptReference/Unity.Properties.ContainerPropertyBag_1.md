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

# ContainerPropertyBag<T0>

class in Unity.Properties

/

Inherits
from:[Unity.Properties.PropertyBag_1](Unity.Properties.PropertyBag_1.html)

/

Implemented
in:[UnityEngine.PropertiesModule](UnityEngine.PropertiesModule.html)

Leave feedback

  

Implements
interfaces:[INamedProperties<T0>](Unity.Properties.INamedProperties_1.html)

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

Base class for implementing a static property bag for a specified container
type. This is an abstract class.

A ContainerPropertyBag_1 is used to describe and traverse the properties for a
specified `TContainer` type.  
  
In order for properties to operate on a type, a ContainerPropertyBag_1 must
exist and be pre-registered for that type.  
  
_NOTE_ In editor use cases property bags can be generated dynamically through
reflection. (see Unity.Properties.Reflection)

### Public Methods

[TryGetProperty](Unity.Properties.ContainerPropertyBag_1.TryGetProperty.html)|
Gets the property associated with the specified name.  
---|---  
  
### Protected Methods

[AddProperty](Unity.Properties.ContainerPropertyBag_1.AddProperty.html)|  Adds
a Property_2 to the property bag.  
---|---  
  
### Inherited Members

### Properties

[InstantiationKind](Unity.Properties.PropertyBag_1.InstantiationKind.html)|
Implement this property and return true to provide custom type instantiation
for the container type.  
---|---  
  
### Public Methods

[Accept](Unity.Properties.PropertyBag_1.Accept.html)|  Accepts visitation from
a specified ITypeVisitor.  
---|---  
[CreateInstance](Unity.Properties.PropertyBag_1.CreateInstance.html)|  Creates
and returns a new instance of TContainer.  
[GetProperties](Unity.Properties.PropertyBag_1.GetProperties.html)|  Implement
this method to return a PropertyCollection_1 that can enumerate through all
properties for the TContainer.  
[TryCreateInstance](Unity.Properties.PropertyBag_1.TryCreateInstance.html)|
Tries to create a new instance of TContainer.  
  
### Protected Methods

[Instantiate](Unity.Properties.PropertyBag_1.Instantiate.html)|  Implement
this method to provide custom type instantiation for the container type.  
---|---  
  
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

