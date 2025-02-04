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

# ConverterGroup

class in UnityEngine.UIElements

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

A type to hold information about a conversion registry used locally on
bindings.

You can apply converter groups on a [DataBinding](UIElements.DataBinding.html)
in UXML with the `source-to-ui-converters` or `ui-to-source-converters`
attributes or in C# script with the
[DataBinding.ApplyConverterGroupToSource](UIElements.DataBinding.ApplyConverterGroupToSource.html)
or
[DataBinding.ApplyConverterGroupToUI](UIElements.DataBinding.ApplyConverterGroupToUI.html)
methods.

### Properties

[description](UIElements.ConverterGroup-description.html)|  Optional
description for a converter group ID that may include information about what
this group contains or is used for, to be displayed to users to assist while
authoring.  
---|---  
[displayName](UIElements.ConverterGroup-displayName.html)|  Optional and
alternative name for a converter group ID, to be displayed to users to assist
while authoring.  
[id](UIElements.ConverterGroup-id.html)|  The group id.  
  
### Constructors

[ConverterGroup](UIElements.ConverterGroup-ctor.html)|  Creates a
ConverterGroup.  
---|---  
  
### Public Methods

[AddConverter](UIElements.ConverterGroup.AddConverter.html)|  Adds a converter
to the group.  
---|---  
[TryConvert](UIElements.ConverterGroup.TryConvert.html)|  Converts the
specified value from TSource to TDestination using only the converter group.  
[TrySetValue](UIElements.ConverterGroup.TrySetValue.html)|  Sets the value of
a property at the given path to the given value, using this converter group or
the global ones.  
  
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

