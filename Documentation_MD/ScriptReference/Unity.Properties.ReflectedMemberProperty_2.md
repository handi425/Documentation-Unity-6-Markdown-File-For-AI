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

# ReflectedMemberProperty<T0,T1>

class in Unity.Properties

/

Inherits from:[Unity.Properties.Property_2](Unity.Properties.Property_2.html)

/

Implemented
in:[UnityEngine.PropertiesModule](UnityEngine.PropertiesModule.html)

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

A ReflectedMemberProperty_2 provides strongly typed access to an underlying
FieldInfo or PropertyInfo object.

The implementation uses slow reflection calls internally. This is intended to
be used as an intermediate solution for quick editor iteration.

### Constructors

[ReflectedMemberProperty_2](Unity.Properties.ReflectedMemberProperty_2-ctor.html)|
Initializes a new ReflectedMemberProperty_2 instance for the specified
FieldInfo.  
---|---  
  
### Inherited Members

### Properties

[IsReadOnly](Unity.Properties.Property_2.IsReadOnly.html)|  Gets a value
indicating whether the property is read-only or not.  
---|---  
[Name](Unity.Properties.Property_2.Name.html)|  Gets the name of the property.  
  
### Public Methods

[Accept](Unity.Properties.Property_2.Accept.html)|  Call this method to invoke
IPropertyVisitor.Visit_2 with the strongly typed container and value.  
---|---  
[DeclaredValueType](Unity.Properties.Property_2.DeclaredValueType.html)|
Returns the declared value type of the property.  
[GetAttribute](Unity.Properties.Property_2.GetAttribute.html)|  Returns the
first attribute of the given type.  
[GetAttributes](Unity.Properties.Property_2.GetAttributes.html)|  Returns all
attribute of the given type.  
[GetValue](Unity.Properties.Property_2.GetValue.html)|  Returns the property
value of a specified container.  
[HasAttribute](Unity.Properties.Property_2.HasAttribute.html)|  Returns true
if the property has any attributes of the given type.  
[SetValue](Unity.Properties.Property_2.SetValue.html)|  Sets the property
value of a specified container.  
  
### Protected Methods

[AddAttribute](Unity.Properties.Property_2.AddAttribute.html)|  Adds an
attribute to the property.  
---|---  
[AddAttributes](Unity.Properties.Property_2.AddAttributes.html)|  Adds a set
of attributes to the property.  
  
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

